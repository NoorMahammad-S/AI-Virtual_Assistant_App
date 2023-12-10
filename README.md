# AI-Virtual Assistant App

This AI-Virtual_Assistant App contains a Flask web application that utilizes speech recognition to process user commands. The application can perform various tasks such as checking the current time, booking flights, ordering groceries, telling jokes, and providing weather forecasts.

## Prerequisites

Before running the application, ensure that you have the following dependencies installed:

- Python 3.x
- Flask
- SpeechRecognition
- pyttsx3
- requests

Install the dependencies using the following command:

```bash
pip install flask SpeechRecognition pyttsx3 requests
```

## Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/NoorMahammad-S/AI-Virtual_Assistant_App.git
cd AI-Virtual_Assistant_App
```

2. Run the Flask application:

```bash
python app.py
```

The application will be accessible at `http://localhost:5000` in your web browser.

## Usage

1. Open the application in your web browser.

2. Enter a command in the provided input field (e.g., "What's the time?", "Book a flight to Paris", "Order groceries", etc.).

3. Click the "Submit" button to process the command.

4. The application will respond accordingly, utilizing speech synthesis to provide feedback.

## Features

- Speech recognition for command input
- Integration with external APIs for flight booking and grocery ordering
- Time, joke, and weather forecast functionalities
- Responsive web interface

## Configuration

Ensure to set up API keys for the flight and grocery APIs using OpenAI Secret Manager. Replace the placeholder API endpoints in the code with the actual endpoints.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to add.

## Acknowledgments

- Thanks to the developers of Flask, SpeechRecognition, and other libraries used in this project.
