# flask run --port=8080 --debug

from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import requests
import mysql.connector

db_infos = {"host" : "localhost", "user":"root", "password":"", "database":"sae_api"}



app = Flask(__name__)
app.secret_key = b'veigar'


base_url = "http://127.0.0.1:5000/api/"
default_pfp = "/static/images/default_pfp.png"


temp_stockage = {"you" : {"Chracter": None}, "stats" : {"hp" : 0, "att": 0, "def": 0, "speed": 0, "ki":0}, "opponent" : {"Chracter": None}, "stats" : {"hp" : 0, "att": 0, "def": 0, "speed": 0, "ki":0}, "stage" : None}


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
    if not 'user_id' in session:
        return render_template('/register.html')
    # todo
    else:
        return redirect('/')

    # TO DO IMPORTANT 

    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     if email and password:
    #         user = verify_credentials(email, password)
    #         if user:
    #             session['user_id'] = user['id']
    #             session['profile_picture'] = user['profile_picture']
    #             return redirect('/')
    #         else:
    #             return render_template('register.html', error="Identifiants incorrects. Veuillez réessayer.")

    # return render_template('register.html', error="")


@app.route('/profile')
def profile():
    if 'user_id' in session:
        return render_template('profile.html')
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
        print(session)

        required_params = ['yourPick', 'ennemy', 'stage']
        missing_params = [param for param in required_params if param not in query_params]

        if missing_params:
            return redirect('/')

        yourPick = requests.get(f"{base_url}characters/{query_params['yourPick']}").json()
        ennemy = requests.get(f"{base_url}characters/{query_params['ennemy']}").json()
        stage = requests.get(f"{base_url}stages/{query_params['stage']}").json()

        return render_template('game/modes/custom_game.html', yourPick=yourPick, ennemy=ennemy, stage=stage)

    else:
        return redirect('/')



# --------------------------EXEMPLE REQUEST FROM API---------------------------
# @app.route('/<string:email>')
# def index_user(email):
#     request = requests.get(base_url + f"userInfos/{email}")
#     user = request.json()
#     return user


