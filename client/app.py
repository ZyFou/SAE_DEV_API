# flask run --port=8080 --debug

from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import requests
import mysql.connector

db_infos = {"host" : "localhost", "user":"root", "password":"", "database":"sae_api"}

app = Flask(__name__)
app.secret_key = b'veigar'

base_url = "http://127.0.0.1:5000/api/"
default_pfp = "https://i.pinimg.com/474x/3b/65/5e/3b655e1f8aa870ccebce29159b6dd70e.jpg"
default_banner = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr5STtRwhRGtjmno8wvhTi0rklpxHIe44Vj6bBRRV_syAfsdinpR3bTwBPYbE9BZEQ7-k&usqp=CAU"


@app.route('/')
def index():
    pfp = default_pfp
    if 'user_id' in session:
        pfp = session["profile_picture"]
        
        return render_template('index.html', profile_picture=pfp, is_co = True)
    
    else:
        return render_template('index.html', profile_picture=pfp, is_co = False)


def verify_credentials(email, password):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT id, password, profile_picture FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and password == user[1]:
        cursor.close()
        db.close()
        return {'id': user[0], 'profile_picture': user[2]}
    else:
        return None
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            print(password)

            if email and password:
                user = verify_credentials(email, password)
            
                if user:
                    session['user_id'] = user['id']
                    session['profile_picture'] = user['profile_picture']
                    return redirect('/')
                else:
                    return render_template('login.html', error="Identifiants incorrects. Veuillez réessayer.")
            
        else:
            return render_template('login.html', error="")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if the user is not already logged in
    if 'user_id' not in session:
        if request.method == 'POST':
            # Retrieve form data
            pseudo = request.form.get('pseudo')
            email = request.form.get('email')
            password = request.form.get('password')

            if pseudo and email and password:
                try:
                    db = mysql.connector.connect(
                        host=db_infos['host'],
                        user=db_infos['user'],
                        password=db_infos['password'],
                        database=db_infos['database']
                    )
    
                    cursor = db.cursor()

                    # Check if the email is already in use
                    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                    existing_user = cursor.fetchone()
                    if existing_user:
                        # If the email is already in use, show an error message
                        return render_template('register.html', error="Email already in use.")

                    # Insert the new user into the database
                    cursor.execute("""INSERT INTO users (nickname, email, password, admin, profile_picture, banner, experience, level) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)""", 
                                   (pseudo, email, password, False, default_pfp,default_banner, 0,1))
                    db.commit()

                    # Retrieve the ID of the newly inserted user
                    user = verify_credentials(email, password)
                    # Close the cursor and the database connection
                    cursor.close()
                    db.close()

                    # Store the user ID in the session
                    session['user_id'] = user['id']
                    session['profile_picture'] = user['profile_picture']


                    # Redirect the user to the home page
                    return redirect('/')
                    
                except mysql.connector.Error as err:
                    # If there's an error interacting with the database, show an error message
                    return render_template('register.html', error="Error registering. Please try again.")

        # If the request method is GET, simply display the registration form
        return render_template('register.html', error="")
    else:
        # If the user is already logged in, redirect them to the home page
        return redirect('/')

    


@app.route('/profile' , methods=['GET', 'POST'])
def profile():
    if 'user_id' in session:

        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        if request.method == 'POST':

            nickname = request.form.get('nickname')
            bio = request.form.get('bio')
            email = request.form.get('email')
            password = request.form.get('password')

            new_pfp = request.form.get('pfp_url')
            if not new_pfp:
                cursor.execute("SELECT profile_picture FROM users WHERE id = %s", (session["user_id"],))
                pfp = cursor.fetchone()
                new_pfp =  pfp[0]

            session['profile_picture'] = new_pfp
            
            new_banner = request.form.get('banner_url')
            if not new_banner:
                cursor.execute("SELECT banner FROM users WHERE id = %s", (session["user_id"],))
                banner = cursor.fetchone()
                new_banner =  banner[0]


            if not password:
                cursor.execute("SELECT password FROM users WHERE id = %s", (session["user_id"],))
                pwd = cursor.fetchone()
                password =  pwd[0]

            cursor.execute("UPDATE users SET nickname = %s, email = %s, bio = %s, profile_picture = %s, banner = %s, password = %s WHERE id = %s", (nickname, email, bio, new_pfp, new_banner, password, session["user_id"]))
            db.commit()
            
            cursor.close()
            db.close()

            return redirect('/profile')
    
        cursor.execute("SELECT nickname, email, bio, profile_picture, banner FROM users WHERE id = %s", (session["user_id"],))
        userinfos = cursor.fetchone()
        userinfos = {"nickname":userinfos[0],
                     "email":userinfos[1],
                     "bio":userinfos[2],
                     "profile_picture":userinfos[3],
                     "banner":userinfos[4]}

        cursor.close()
        db.close()

        return render_template('profile.html', userinfos = userinfos)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


@app.route('/gameMode')
def gameMode():
    if 'user_id' in session:
        return render_template('game/gameMode.html')
    else:
        return redirect('/')
    


@app.route('/gameMode/custom')
def gameMode_Custom():
    if 'user_id' in session:
        characters_response = requests.get(base_url + "characters")
        characters = characters_response.json()

        stages_response = requests.get(base_url + "stages")
        stages = stages_response.json()
        return render_template('game/modes/custom.html', characters=characters, stages=stages)
    else:
        return redirect('/')
        
    

# FAIRE LA SESSION

@app.route('/gameMode/customGame')
def testGame():
    if 'user_id' in session:
        query_params = request.args
        # print(session)

        required_params = ['yourPick', 'ennemy', 'stage', 'mode']
        missing_params = [param for param in required_params if param not in query_params]

        if missing_params:
            return redirect('/')

        yourPick = requests.get(f"{base_url}characters/{query_params['yourPick']}").json()
        yourPick_techniques = requests.get(f"{base_url}TOB/{yourPick['idCharacter']}").json()
        yourPick_tech_list = {}

        for tech_id in yourPick_techniques['idTechniques']:
            infos = requests.get(f"{base_url}techniques/{tech_id}").json()
            yourPick_tech_list[infos['name']] = infos


        ennemy = requests.get(f"{base_url}characters/{query_params['ennemy']}").json()
        ennemy_techniques = requests.get(f"{base_url}TOB/{ennemy['idCharacter']}").json()
        ennemy_tech_list = {}

        for tech_id in ennemy_techniques['idTechniques']:
            infos = requests.get(f"{base_url}techniques/{tech_id}").json()
            ennemy_tech_list[infos['name']] = infos
        

        stage = requests.get(f"{base_url}stages/{query_params['stage']}").json()
        mode = query_params['mode']

        return render_template('game/modes/custom_game.html', yourPick=yourPick, yourPick_tech_list=yourPick_tech_list, ennemy=ennemy, ennemy_tech_list=ennemy_tech_list, stage=stage, mode=mode)

    else:
        return redirect('/')

