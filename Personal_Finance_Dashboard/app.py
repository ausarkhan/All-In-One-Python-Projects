"""
Personal Finance Dashboard (Issue #93)
Minimal Flask backend + HTML/JS frontend with Chart.js
"""
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

DATA = {
    "expenses": [],
    "budget": 0
}

@app.route("/api/expenses", methods=["GET", "POST"])
def expenses():
    if request.method == "POST":
        expense = request.json
        DATA["expenses"].append(expense)
        return jsonify({"status": "added"}), 201
    return jsonify(DATA["expenses"])

@app.route("/api/budget", methods=["GET", "POST"])
def budget():
    if request.method == "POST":
        DATA["budget"] = request.json.get("budget", 0)
        return jsonify({"status": "set"}), 201
    return jsonify({"budget": DATA["budget"]})

@app.route("/")
def index():
    return send_from_directory(".", "dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
