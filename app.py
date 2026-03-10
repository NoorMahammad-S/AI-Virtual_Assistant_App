from flask import Flask, render_template, request, jsonify
import requests
import pyttsx3
import datetime
import logging

app = Flask(__name__)

engine = pyttsx3.init()

WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url).json()

        if response["cod"] != 200:
            return "City not found."

        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]

        result = f"The temperature in {city} is {temp}°C with {desc}."
        speak(result)
        return result

    except Exception as e:
        logging.error(e)
        return "Unable to fetch weather."


def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    speak(joke)
    return joke


def process_command(command):

    command = command.lower()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {current_time}"

    elif "joke" in command:
        response = tell_joke()

    elif "book a flight to" in command:
        destination = command.replace("book a flight to", "").strip()
        response = f"Flight booking request sent for {destination}"

    elif "order groceries" in command:
        items = command.replace("order groceries", "").strip()
        response = f"Groceries ordered: {items}"

    elif "weather" in command:
        city = command.replace("weather in", "").strip()
        response = get_weather(city)

    else:
        response = "Sorry, I didn't understand that command."

    speak(response)

    return response


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process_command", methods=["POST"])
def command():

    command = request.form["command"]

    result = process_command(command)

    return jsonify({"response": result})


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
