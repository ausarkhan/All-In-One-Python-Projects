"""
Travel Itinerary Planner (Issue #92)
Minimal Flask backend + HTML/JS frontend with Google Maps embed
"""
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

ITINERARIES = []

@app.route("/api/itineraries", methods=["GET", "POST"])
def itineraries():
    if request.method == "POST":
        itinerary = request.json
        ITINERARIES.append(itinerary)
        return jsonify({"status": "added"}), 201
    return jsonify(ITINERARIES)

@app.route("/")
def index():
    return send_from_directory(".", "planner.html")

if __name__ == "__main__":
    app.run(debug=True)
