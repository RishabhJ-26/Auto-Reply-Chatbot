# Auto Reply Chatbot 🤖

Hey there! I'm Rishabh, and this is a fun little project I built called **Auto Reply Chatbot**.

It's a Python-based chatbot that automatically reads the latest chat message from the screen (like WhatsApp Web), sends it to Google's Gemini AI, and replies in **Hinglish**—just like a real person would. The bot even replies as *me*, so it's like Rishabh is chatting with you in real time 😄

---

## 🚀 What It Does

- Reads the most recent chat message using `PyAutoGUI`
- Uses Gemini AI to generate a smart, Hinglish-style reply
- Automatically pastes and sends the message—no hands needed!
- Sounds like a real human (okay, sounds like **me**, Rishabh 😄)

---

## 🧠 Tech Stack

- 🐍 **Python**
- 🖱️ **PyAutoGUI** – for mouse/keyboard automation
- 📋 **Pyperclip** – for clipboard handling
- 🤖 **Google Generative AI (Gemini)** – for generating replies

---

## 🔧 How to Use

> ⚠️ This project uses screen automation, so you might need to tweak the coordinates based on your screen resolution and chat layout.

1. Clone this repo:
   ```
   git clone https://github.com/RishabhJ-26/Auto-Reply-Chatbot.git
   cd Auto-Reply-Chatbot
   ```
2. Install the required packages:

```
pip install pyautogui pyperclip google-generativeai
```

3. Add your Gemini API key:

```
genai.configure(api_key="YOUR_API_KEY")
```

4. Run the script:

```
python chatbot.py
```

📹 Demo (coming soon...)
I'll add a short demo video or GIF soon to show how it works in action!

💬 Why I Made This
I wanted to explore automation + AI in a fun way, and I thought—what if I could build a bot that chats just like me? So I gave it my personality, my language style (Hinglish ftw 😎), and some basic logic to make conversations feel human.

🙌 Let's Connect
If you're into AI, automation, or just like building cool side projects, feel free to connect with me:

GitHub: @RishabhJ-26

LinkedIn: @rishabh-jain-enris

If you liked this repo, don’t forget to ⭐ it!

Thanks for reading. Happy coding! 😄
