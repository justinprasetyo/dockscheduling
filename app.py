from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

from database import dock_dict, make_reservation, delete_reservation
from check import check_size

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/reservations', methods=['POST'])
def get_available():
    data = request.get_json() 

    if data is None:
        return jsonify({"error": "No valid data received"}), 400

    result = {"dock": False, "size": False, "date": False}
    if check_size(data["dock_number"], data["length"], data["width"]):
        result["size"] = True
    else:
        return jsonify(f"Sizing does not fit dock: ({dock_dict[int(data["dock_number"]) - 1]["length"]}ft x {dock_dict[int(data["dock_number"]) - 1]["width"]}ft)")

    make_reservation(data["dock_number"], data["start_date"], data["end_date"], data["reason"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8080, debug=True)