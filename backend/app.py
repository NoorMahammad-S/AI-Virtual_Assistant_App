import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import pyttsx3

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        message = data.get("message")

        if not message:
            return jsonify({"reply": "No message received."})

        # OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":message}]
        )

        reply = response.choices[0].message.content.strip()

        # Speak the response
        speak(reply)

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)