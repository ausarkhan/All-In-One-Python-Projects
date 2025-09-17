"""
Language Learning Chatbot (Issue #90)
Minimal Flask backend + HTML/JS frontend using OpenAI API
"""
from flask import Flask, request, jsonify, send_from_directory
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")  # Replace with your key or set as env var

@app.route("/api/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    prompt = f"You are a helpful language learning assistant. Help the user practice and learn languages.\nUser: {user_msg}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    reply = response.choices[0].text.strip()
    return jsonify({"reply": reply})

@app.route("/")
def index():
    return send_from_directory(".", "chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)
