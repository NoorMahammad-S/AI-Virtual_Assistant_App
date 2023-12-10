from flask import Flask, render_template, request, jsonify
import openai_secret_manager
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import logging

app = Flask(__name__)

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError as e:
            speak(f"Speech recognition request failed: {e}")
            return ""

def process_command(command):
    try:
        if "what's the time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif "book a flight to" in command:
            destination = command.split("book a flight to ")[1]
            speak(f"Booking a flight to {destination}. When would you like to travel?")
            date = listen()
            book_flight(destination, date)
        elif "order groceries" in command:
            speak("Sure! What items would you like to order?")
            items = listen()
            order_groceries(items)
        elif "tell me a joke" in command:
            joke = "Why don't scientists trust atoms? Because they make up everything!"
            speak(joke)
        elif "weather forecast" in command:
            speak("Sure! Please provide the city for the weather forecast.")
            city = listen()
            get_weather_forecast(city)
        else:
            speak("Sorry, I don't understand that command.")
    except Exception as e:
        logging.error(f"Error processing command: {e}")
        speak("Sorry, there was an error processing your command.")

def book_flight(destination, date):
    try:
        api_key = openai_secret_manager.get_secret("flight_api")["api_key"]
        api_endpoint = "https://api.example.com/book-flight"
        params = {"destination": destination, "date": date, "api_key": api_key}
        response = requests.post(api_endpoint, params=params)
        response.raise_for_status()
        speak(f"Flight to {destination} booked successfully for {date}.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Flight booking failed: {e}")
        speak("Sorry, there was an issue booking the flight. Please try again.")

def order_groceries(items):
    try:
        api_key = openai_secret_manager.get_secret("grocery_api")["api_key"]
        api_endpoint = "https://api.example.com/order-groceries"
        params = {"items": items, "api_key": api_key}
        response = requests.post(api_endpoint, params=params)
        response.raise_for_status()
        speak(f"Groceries ({items}) ordered successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Grocery order failed: {e}")
        speak("Sorry, there was an issue ordering groceries. Please try again.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command_route():
    try:
        command = request.form['command']
        process_command(command)
        return jsonify({'response': 'Command processed successfully'})
    except Exception as e:
        logging.error(f"Error processing command route: {e}")
        return jsonify({'response': 'Error processing command'})

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
