const messagesContainer = document.getElementById("messages");
const input = document.getElementById("user-input");
const form = document.getElementById("chat-form");

// اطمینان از اینکه JS بعد از لود HTML اجرا می‌شه
document.addEventListener("DOMContentLoaded", () => {
  form.addEventListener("submit", async function (e) {
    e.preventDefault();  // جلوگیری از ری‌فرش صفحه
    await sendMessage();
  });
});

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  // پیام کاربر
  addMessage(text, "user");
  input.value = "";
  input.disabled = true;

  try {
    const response = await fetch("http://127.0.0.1:8000/chat_with_memory", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    const data = await response.json();
    console.log("📩 پاسخ از سرور:", data);

    if (data.reply) {
      addMessage(data.reply, "assistant");
    } else if (data.error) {
      addMessage(`⚠️ خطا از سرور: ${data.error}`, "assistant");
    } else {
      addMessage("❗ پاسخی از سرور دریافت نشد.", "assistant");
    }
  } catch (err) {
    console.error("❌ خطای اتصال:", err);
    addMessage("❌ خطا در اتصال به سرور", "assistant");
  }

  input.disabled = false;
  input.focus();
}

// تابع افزودن پیام به صفحه بدون پاک کردن قبلی‌ها
function addMessage(text, role) {
  const msgDiv = document.createElement("div");
  msgDiv.className = `message ${role}`;
  msgDiv.textContent = text;
  messagesContainer.appendChild(msgDiv);
  
  // اسکرول به پایین
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
