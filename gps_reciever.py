from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

latest_location = {
    "latitude": None,
    "longitude": None,
    "timestamp": None
}

location_lock = threading.Lock()


# Receive GPS location
@app.route('/location', methods=['POST'])
def receive_location():

    data = request.json

    lat = data.get('latitude')
    lon = data.get('longitude')

    if lat is None or lon is None:
        return jsonify({
            "error": "Latitude or longitude missing"
        }), 400

    with location_lock:
        latest_location["latitude"] = float(lat)
        latest_location["longitude"] = float(lon)
        latest_location["timestamp"] = time.time()

    print("\nReceived GPS Location:")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")

    return "Location received successfully"


# Return latest GPS location
@app.route('/latest-location', methods=['GET'])
def get_latest_location():

    with location_lock:
        location = latest_location.copy()

    if location["latitude"] is None:
        return jsonify({
            "error": "No GPS location available"
        }), 404

    return jsonify(location)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)