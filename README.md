# 🤖 AI Virtual Assistant (React + Flask + OpenAI GPT)

![React](https://img.shields.io/badge/React-17.x-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-3.5-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A **full-stack AI Virtual Assistant** with a **ChatGPT-style interface**, **real-time voice input/output**, and **dynamic AI responses** using **OpenAI GPT-3.5**.

This project demonstrates how to build a **modern AI assistant** that can:

* 🎤 Accept **voice input** or typed commands
* 🧠 Provide **AI-powered responses** using OpenAI
* 🔊 Speak responses aloud with **text-to-speech**
* 🌤 Provide **weather forecasts**
* ⏰ Tell the **current time**
* 😂 Tell **jokes**
* 📜 Maintain a **chat-style conversation**

Ideal for developers learning **full-stack AI applications, voice assistants, React + Flask integration, and OpenAI APIs**.

---

## 📚 Table of Contents

* Overview
* Features
* Tech Stack
* Project Architecture
* Installation
* Usage
* Deployment
* Example Commands
* Future Improvements
* Contributing
* License
* Acknowledgments

---

## 🚀 Overview

This AI Virtual Assistant is a **React frontend + Flask backend project** that combines:

* **ChatGPT-style chat UI**
* **Voice input** (microphone)
* **Text-to-speech output**
* **Dynamic AI responses via OpenAI GPT-3.5**

Users can interact with the assistant by typing or speaking commands. The assistant responds **in real-time with text and speech**, providing an **interactive and modern AI experience**.

---

## ✨ Features

* 💬 **ChatGPT-style UI** with scrollable conversation
* 🎤 **Voice input** using browser microphone
* 🔊 **Voice output** using `pyttsx3` or browser TTS
* 🧠 **AI-powered responses** using OpenAI GPT-3.5
* 🌤 Weather forecast integration
* ⏰ Current time queries
* 😂 Joke generation
* 🖥 Fully responsive for **desktop and mobile**
* ⚡ Clean and modern UI
* 🔧 Easy to extend for additional AI features

---

## 🛠 Tech Stack

**Frontend:**

* React
* Web Speech API (Voice input)
* HTML/CSS for chat UI

**Backend:**

* Python 3
* Flask
* Flask-CORS
* pyttsx3 (Text-to-Speech)
* OpenAI API

**Concepts Used:**

* Voice recognition
* Speech synthesis
* REST API integration
* Dynamic AI responses
* Full-stack web development

---

## 📁 Project Architecture

```text
AI-Virtual-Assistant-App/
│
├── backend/                  # Flask backend
│   ├── app.py                # API for AI chat & TTS
│   ├── requirements.txt
│   └── .env                  # OpenAI API key
│
├── frontend/                 # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat.js
│   │   │   ├── Message.js
│   │   │   └── VoiceButton.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NoorMahammad-S/AI-Virtual-Assistant-App.git
cd AI-Virtual-Assistant-App
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the backend folder:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

Start the backend server:

```bash
python app.py
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Open your browser at:

```
http://localhost:3000
```

---

## ▶️ Usage

* Type a message or click the **🎤 Speak** button to send a voice command.
* Example commands:

```text
Hello
Tell me a joke
What's the weather in London?
What's the time?
Book a flight to Paris
```

* The assistant responds **in text and voice**.

---

## 🌐 Deployment

You can deploy:

* **Frontend:** Vercel / Netlify
* **Backend:** Render / AWS / Railway

Make sure the **backend URL** is correctly set in React’s fetch calls for production.

---

## 🚧 Future Improvements

* 🧠 Integrate **advanced OpenAI GPT-4**
* 📱 Mobile-optimized interface with responsive design
* 📊 Save **conversation history**
* 🌐 Multi-language support
* ☁️ Dockerized deployment for easy scaling
* 🔊 Browser-based TTS for better voice output

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch:

```bash
git checkout -b feature/new-feature
```

3. Commit your changes:

```bash
git commit -m "Add new feature"
```

4. Push the branch:

```bash
git push origin feature/new-feature
```

5. Open a Pull Request 🚀

---

## 📜 License

This project is licensed under **MIT License**.

---

## 🙏 Acknowledgments

Special thanks to:

* [OpenAI](https://openai.com/) for GPT API
* [Flask](https://flask.palletsprojects.com/)
* [React](https://reactjs.org/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

