"""
Sustainable Travel Planner (Issue #91)
Minimal Flask backend + HTML/JS frontend
"""
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

SUGGESTIONS = [
    {"destination": "Amsterdam", "activity": "Bike tours, local markets", "eco_score": 9},
    {"destination": "Costa Rica", "activity": "Rainforest hikes, eco-lodges", "eco_score": 10},
    {"destination": "Kyoto", "activity": "Temple visits, public transport", "eco_score": 8},
    {"destination": "Vancouver", "activity": "Urban parks, cycling", "eco_score": 8},
    {"destination": "New Zealand", "activity": "Nature reserves, local farms", "eco_score": 9}
]

@app.route("/api/suggestions", methods=["GET"])
def suggestions():
    return jsonify(SUGGESTIONS)

@app.route("/")
def index():
    return send_from_directory(".", "sustainable.html")

if __name__ == "__main__":
    app.run(debug=True)
