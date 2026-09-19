from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

from database import dock_dict, make_reservation, delete_reservation, get_allreservations
from check import check_size, check_date

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

    if "delete" in data and data["delete"]:
        delete_reservation(data["dock_number"], data["start_date"], data["end_date"])
        get_allreservations()
        return '', 204

    #calculate other available docks too with proper sizing and dates if results in error
    result = {"available-docks": [], "size": False, "date": False}

    sizecheck = check_size(data["dock_number"], data["length"], data["width"])
    if sizecheck:
        result["size"] = True
    else:
        return jsonify(f"Sizing does not fit dock: ({dock_dict[int(data["dock_number"]) - 1]["length"]}ft x {dock_dict[int(data["dock_number"]) - 1]["width"]}ft)")

    #datecheck = check_date(data["dock_number"], data["start_date"], data["end_date"])
    #if datecheck == True:
    #    result["date"] = True
    #else:
    #    return jsonify(f"Timeframe already booked: (**overlapping dates**)")

    #make make-reservation into a yes or no button with a pop-up
    make_reservation(data["dock_number"], data["start_date"], data["end_date"], data["reason"])
    get_allreservations()
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8080, debug=True)