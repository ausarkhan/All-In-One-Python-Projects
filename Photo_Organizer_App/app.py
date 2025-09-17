"""
Photo Organizer App (Issue #89)
Minimal Flask backend + HTML/JS frontend
"""
from flask import Flask, request, jsonify, send_from_directory, render_template_string
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "photos"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

PHOTOS = []

@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files['photo']
    tags = request.form.get('tags', '')
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    meta = {
        "filename": filename,
        "date": datetime.now().strftime('%Y-%m-%d'),
        "tags": tags.split(',') if tags else []
    }
    PHOTOS.append(meta)
    return jsonify({"status": "uploaded"})

@app.route("/api/photos", methods=["GET"])
def get_photos():
    tag = request.args.get('tag')
    date = request.args.get('date')
    results = PHOTOS
    if tag:
        results = [p for p in results if tag in p['tags']]
    if date:
        results = [p for p in results if p['date'] == date]
    return jsonify(results)

@app.route("/photos/<filename>")
def serve_photo(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/")
def index():
    return send_from_directory(".", "organizer.html")

if __name__ == "__main__":
    app.run(debug=True)
