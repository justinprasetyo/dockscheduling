from flask import Flask, request, jsonify
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)