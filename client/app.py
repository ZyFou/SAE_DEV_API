# flask run --port=8080 --debug

from flask import Flask, render_template
import requests
app = Flask(__name__)

base_url = "http://127.0.0.1:5000/api/"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:name>')
def index_user(name):
    request = requests.get(base_url + f"infos/{name}")
    user = request.json()
    return render_template('index.html', user=user)




# def get_pokemon_details(name):
#     # Effectuer une requête pour obtenir les détails d'un Pokémon
#     response = requests.get(POKEAPI_BASE_URL + f'pokemon/{name}')
#     pokemon = response.json()
#     return pokemon


# @app.route('/pokemon/<string:name>')
# def pokemon_detail(name):
#     pokemon = get_pokemon_details(name)
#     return render_template('detail.html', pokemon=pokemon)
    