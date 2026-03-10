# 🤖 AI Virtual Assistant App (Flask + Speech Recognition)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An **AI-powered Virtual Assistant Web Application** built with **Python and Flask** that processes **voice and text commands** using speech recognition.

This project demonstrates how to build a **voice-enabled AI assistant** capable of performing multiple tasks such as:

* Checking the **current time**
* Providing **weather forecasts**
* **Booking flights**
* **Ordering groceries**
* Telling **jokes**
* Responding to **user commands using speech synthesis**

This repository is ideal for developers who want to learn how to build a **Python AI assistant, voice recognition system, or Flask-based AI web app**.

---

# 📚 Table of Contents

* Overview
* Features
* Tech Stack
* Project Structure
* Installation
* Usage
* Configuration
* Future Improvements
* Contributing
* License
* Acknowledgments

---

# 🚀 Overview

The **AI Virtual Assistant App** is a **Flask-based web application** that integrates **speech recognition and text-to-speech technologies** to create a simple intelligent assistant.

Users can interact with the assistant through a web interface by entering commands such as:

```
What's the time?
Tell me a joke
Book a flight to Paris
Order groceries
What's the weather today?
```

The assistant processes the command and responds with **audio feedback using speech synthesis**.

This project is useful for learning:

* AI assistant development
* Python voice recognition
* Flask web application development
* API integration
* Text-to-speech systems

---

# ✨ Features

✔ Voice command processing using **SpeechRecognition**
✔ AI assistant responses using **Text-to-Speech (pyttsx3)**
✔ Web interface powered by **Flask**
✔ Weather information retrieval
✔ Joke generator
✔ Flight booking API integration
✔ Grocery ordering integration
✔ Time query functionality
✔ Extensible architecture for adding new AI features

---

# 🛠 Tech Stack

**Backend**

* Python 3
* Flask

**Libraries**

* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* requests (API communication)

**Concepts Used**

* Voice recognition
* Speech synthesis
* REST API integration
* Web application development

---

# 📁 Project Structure

```
AI-Virtual_Assistant_App
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
├── static/               # CSS, JS, assets
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

# ⚙️ Installation

Follow these steps to run the project locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/NoorMahammad-S/AI-Virtual_Assistant_App.git
cd AI-Virtual_Assistant_App
```

## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install flask SpeechRecognition pyttsx3 requests
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

---

# 🧠 How It Works

1. The user enters a command through the web interface.
2. The application processes the input using **SpeechRecognition**.
3. The command is interpreted by the backend logic.
4. The assistant performs the requested task.
5. The response is returned as **text and speech output** using **pyttsx3**.

---

# 🔑 Configuration

Some features require **API keys**, such as:

* Flight booking APIs
* Weather APIs
* Grocery ordering services

Steps:

1. Obtain API keys from the respective service providers.
2. Store them securely using **environment variables** or a **secret manager**.
3. Replace placeholder endpoints in the code with actual API URLs.

Example:

```python
API_KEY = "your_api_key_here"
```

---

# 🚧 Future Improvements

Potential enhancements for this project:

* 🎤 Real-time voice input from browser
* 🤖 Integration with **OpenAI / LLM models**
* 📱 Mobile-friendly interface
* 🧠 Natural Language Processing (NLP)
* 🌐 Multi-language support
* 📊 Conversation history
* ☁️ Cloud deployment (AWS / Docker)

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request 🚀

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgments

Special thanks to the creators of the following open-source libraries:

* Flask
* SpeechRecognition
* pyttsx3
* requests

Their tools make building AI-powered applications significantly easier.
