from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/dimensions', methods=['POST'])
def get_compatible():
    data = request.get_json() 

    if data is None:
        return jsonify({"error": "No valid data received"}), 400
    
    #response = requests.post(
        #'/api/dimensions',
        #json={
            #"compatible": True #for now, calculations later
        #})

    return jsonify({"compatible": True}) #for now, calculations later

@app.route('/api/reservations', methods=['POST'])
def get_available():
    data = request.get_json() 

    if data is None:
        return jsonify({"error": "No valid data received"}), 400
    
    #response = requests.post(
        #'/api/dimensions',
        #json={
            #"compatible": True #for now, calculations later
        #})

    return jsonify({"available": True}) #for now, calculations later

if __name__ == "__main__":
    app.run(port=8080, debug=True)