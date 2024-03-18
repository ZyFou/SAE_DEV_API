# flask run --port=8080 --debug

from flask import Flask, render_template
import requests
app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

response = requests.get(POKEAPI_BASE_URL + "pokemon")

nbPokemons = response.json().get("count")
tabPokemonsAPI = response.json().get('results')



@app.route('/')
def home():
    return render_template('index.html', pokemons=tabPokemonsAPI, nb=nbPokemons)


def get_pokemon_details(name):
    # Effectuer une requête pour obtenir les détails d'un Pokémon
    response = requests.get(POKEAPI_BASE_URL + f'pokemon/{name}')
    pokemon = response.json()
    return pokemon


@app.route('/pokemon/<string:name>')
def pokemon_detail(name):
    pokemon = get_pokemon_details(name)
    return render_template('detail.html', pokemon=pokemon)
    