from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

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
        delete_reservation(data["reservation_id"])
        return '', 204

    #i dont need this for now
    #calculate other available docks too with proper sizing and dates if results in error
    #result = {"available-docks": [], "size": False, "date": False}

    #vessel dimensions input checks
    if data["length"] == '' or data["width"] == '':
        return jsonify("If reserving for a non-vessel event, please type 0 for dimensions.")
    elif float(data["length"]) < 0 or float(data["width"]) < 0:
        return jsonify("Please enter valid numbers.")

    #vessel dimensional fit check
    sizecheck = check_size(data["dock_number"], data["length"], data["width"])
    if sizecheck != True:
        return jsonify(f"Sizing does not fit dock: ({dock_dict[int(data['dock_number']) - 1]['length']}ft x {dock_dict[int(data['dock_number']) - 1]['width']}ft)")

    #date checks
    if data["start_date"] == '' or data["end_date"] == '':
        return jsonify("Please input dates.")
    elif data["start_date"] > data["end_date"]:
        return jsonify(f"Start date must come before or at the end date.")
    
    datecheck = check_date(data["dock_number"], data["start_date"], data["end_date"])
    if datecheck != True:
        err_message = f"Timeframe already booked: "
        for obj in datecheck:
            err_message += f"{obj['start_date']} to {obj['end_date']} (ID: {obj['id']}, reason: {obj['reason']}). "
        return jsonify(err_message)

    #make make-reservation into a yes or no button with a pop-up
    if "confirm_reservation" in data and data["confirm_reservation"]:
        make_reservation(data["dock_number"], data["start_date"], data["end_date"], data["reason"])
        return jsonify({})

    return jsonify({})

@app.route('/api/reservations', methods=['GET'])
def list_reservations():
    rows = get_allreservations()
    for row in rows:
        row["dock_name"] = dock_dict[int(row["dock_number"]) - 1]["name"]
    return jsonify(rows)

if __name__ == "__main__":
    app.run(port=8080, debug=True)