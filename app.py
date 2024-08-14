from flask import Flask, request, jsonify
from flask_cors import CORS  
from message_variation import create_variations
import os

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return "Welcome to the AI Message Variation API!"

@app.route('/favicon.ico')
def favicon():
    return '', 204  

@app.route('/generate_variations', methods=['POST'])
def generate_variations():
    data = request.json
    message = data['message']
    num_variations = data.get('num_variations', 25)
    variations = create_variations(message, num_variations)
    return jsonify(variations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))