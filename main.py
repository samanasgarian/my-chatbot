from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import cohere
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise RuntimeError("❌ COHERE_API_KEY not found! Put it in .env file")

co = cohere.ClientV2(api_key=COHERE_API_KEY)

app = FastAPI(title="Cohere Chatbot API")
app.mount("/frontend", StaticFiles(directory="frontend", html=True  ), name="frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # در حالت تولید بهتره localhost باشه
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str


DB_PATH = "chat_memory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages ORDER BY id")
    msgs = cursor.fetchall()
    conn.close()
    return [{"role": role, "content": [{"type": "text", "text": content}]} for role, content in msgs]

init_db()

# -------------------- مسیر اصلی --------------------
@app.get("/")
def read_root():
    return {"✅ Cohere chat bot is active!"}


# -------------------- روت چت ساده --------------------
@app.post("/chat")
def chat(msg: Message):
    try:
        response = co.chat(
            messages=[{"role": "user", "content": [{"type": "text", "text": msg.message}]}],
            temperature=0.3,
            model="command-a-03-2025"
        )
        assistant_text = response.message.content[0].text
        return {"reply": assistant_text}
    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}


@app.post("/chat_with_memory")
def chat_with_memory(msg: Message):
    try:
        # ذخیره پیام کاربر
        save_message("user", msg.message)

        # گرفتن تاریخچه گفتگو
        conversation_history = get_messages()

        response = co.chat(
            messages=conversation_history,
            temperature=1,
            model="command-a-03-2025"
        )

        assistant_text = response.message.content[0].text

        # ذخیره پاسخ دستیار
        save_message("assistant", assistant_text)

        # ارسال پاسخ به فرانت‌اند
        return {"reply": assistant_text}

    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}
