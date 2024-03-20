# flask run --port=8080 --debug

from flask import Flask, render_template, request, redirect, session
import requests
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sae_api"
)


app = Flask(__name__)
app.secret_key = b'veigar'

base_url = "http://127.0.0.1:5000/api/"
default_pfp = "/static/images/default_pfp.png"


temp_stockage = {"you" : {"Chracter": None}, "stats" : {"hp" : 0, "att": 0, "def": 0, "speed": 0, "ki":0}, "opponent" : {"Chracter": None}, "stats" : {"hp" : 0, "att": 0, "def": 0, "speed": 0, "ki":0}, "stage" : None}


@app.route('/')
def index():
    
    pfp = default_pfp
    if 'user_id' in session:
        user_id = session['user_id']
        pfp = session["profile_picture"]
        
        return render_template('index.html', profile_picture=pfp, is_co = True)
    
    else:
        return render_template('index.html', profile_picture=pfp, is_co = False)


def verify_credentials(email, password):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, password, profile_picture, banner FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user and password == user[1]:
            return {'id': user[0], 'profile_picture': user[2]}
        else:
            return None
    except:
        print("Erreur de connexion à la base de données:")
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            user = verify_credentials(email, password)
        
            if user:
                session['user_id'] = user['id']
                session['profile_picture'] = user['profile_picture']
                return redirect('/')
        
        # Si l'utilisateur n'est pas trouvé ou si les identifiants sont incorrects
        return render_template('login.html', error="Identifiants incorrects. Veuillez réessayer.")
    
    # Rendre le modèle de connexion par défaut si aucune donnée de formulaire n'est envoyée
    return render_template('login.html', error="")



@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return render_template('/register.html')
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
    session.pop('user_id', None)
    session.pop('profile_picture', None)
    return redirect('/')


@app.route('/gameMode')
def gameMode():
    if 'user_id' in session:
        return render_template('game/gameMode.html')
    else:
        return redirect('/')




# --------------------------EXEMPLE REQUEST FROM API---------------------------
# @app.route('/<string:email>')
# def index_user(email):
#     request = requests.get(base_url + f"userInfos/{email}")
#     user = request.json()
#     return user


