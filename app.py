from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin
import random
from utils import load_quotes, filter_by_lang

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    """Menampilkan daftar endpoint yang tersedia."""
    return jsonify({"message": "Endpoints: /quote, /quotes"}) 

@app.route('/quote', methods=['GET'])
@cross_origin()
def get_random_quote():
    """Mengembalikan satu kutipan acak. Bisa difilter dengan parameter `lang`."""
    lang = request.args.get('lang')
    quotes = load_quotes()
    filtered_quotes = filter_by_lang(quotes, lang) if lang else quotes
    return jsonify(random.choice(filtered_quotes))

@app.route('/quotes', methods=['GET'])
@cross_origin()
def get_all_quotes():
    """Mengembalikan seluruh kutipan."""
    quotes = load_quotes()
    return jsonify(quotes)

if __name__ == '__main__':
    app.run(debug=True)
