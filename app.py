import json
from flask import Flask
from flask import render_template, jsonify
from flask import request
from config import API_KEY, API_URL


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # indique les methodes acceptes, si Post n'est pas dedans => error si on submit
def python():
    adress = ''
    story = ''
    if request.method == 'POST' and 'adress' in request.form: # adress est le nane de l'input dans form
        adress = request.form.get('adress') # on récupère l'input et on le met dans la var adress
    if request.method == 'POST' and 'story' in request.form: # adress est le nane de l'input dans form
        story = request.form.get('story') # on récupère l'input et on le met dans la var adress
    return render_template('base.html', adress = adress, story = story) # affectation de la valeur entré par l'user à adress

@app.route('/index')
def result():
    return render_template('index.html')

@app.route('/api/googleMap')
def google_Map():
    dictionnaire = {

    }

# @app.route('/process', methods=['POST'])
# def process():
#     req = request.get_json()
#     parser = Parser(req["user_adress"])
#     run_parser = parser.process()
#     google_map = myMap()
#     d = google_map.get_coordinate(run_parser)
#     return make_response(jsonify(d))

if __name__ == "__main__":
    app.run(debug=True)
