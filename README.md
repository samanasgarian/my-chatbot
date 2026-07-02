# My Chatbot

A simple AI chatbot web application built with **FastAPI**, **Cohere API**, **SQLite**, **HTML**, **CSS**, and **JavaScript**.

## 🚀 Features

* AI chatbot powered by Cohere
* FastAPI backend
* Simple and responsive web interface
* Chat memory stored in SQLite
* REST API endpoints
* Persian-friendly UI
* CORS enabled for frontend communication

## 🛠️ Technologies Used

* Python
* FastAPI
* Cohere API
* SQLite
* HTML
* CSS
* JavaScript

## 📂 Project Structure

```text
my-chatbot/
│
├── main.py              # FastAPI backend
├── init_db.py           # SQLite database initialization
├── chat_memory.db       # Chat memory database
├── index.html           # Frontend page
├── style.css            # Frontend styles
├── script.js            # Frontend logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/samanasgarian/my-chatbot.git
cd my-chatbot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root and add your Cohere API key:

```env
COHERE_API_KEY=your_cohere_api_key
```

## ▶️ Run the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## 📡 API Endpoints

### GET /

Returns a simple message indicating that the API is running.

### POST /chat

Send a message to the chatbot without saving conversation history.

Example:

```json
{
  "message": "Hello!"
}
```

### POST /chat_with_memory

Send a message to the chatbot and save the conversation in SQLite.

Example:

```json
{
  "message": "Hi, how are you?"
}
```

## 📖 About

**My Chatbot** is a lightweight AI chatbot built with FastAPI and Cohere. It demonstrates how to connect a modern web frontend to an AI-powered backend while maintaining conversation history using SQLite. The project is suitable for learning FastAPI, REST APIs, frontend-backend integration, and AI application development.

## 👨‍💻 Author

**Saman Asgarian**

GitHub: https://github.com/samanasgarian
