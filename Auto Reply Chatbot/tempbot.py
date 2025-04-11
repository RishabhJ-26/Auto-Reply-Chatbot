import pyautogui
import time
import pyperclip
import google.generativeai as genai

genai.configure(api_key="AIzaSyADvuE98G4MRDkWKswilA_LJOkTmvu1q_g")

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

# Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1315, 1051)
time.sleep(2)  # Increased wait time to ensure the click is registered

# Bring the Chrome window to the foreground
pyautogui.hotkey('alt', 'tab')  # Switch to the last active window (Chrome)

# Step 2: Drag the mouse to select the text
pyautogui.moveTo(683, 256)
time.sleep(0.5)
pyautogui.dragTo(1735, 856, duration=2.0, button='left')  # Drag for 1 second
time.sleep(0.5)

# Step 3: Copy the selected text to the clipboard
pyperclip.copy("") 
pyautogui.hotkey('ctrl','c')
time.sleep(2)  # Increased wait time for the copy command to complete

# Step 4: Retrieve the text from the clipboard
chat_history = pyperclip.paste()

# Debugging output to verify copied text
if chat_history:
    print("Copied text:")
    print(chat_history)
else:
    print("No text copied. Please check the selection process.")

def aiProcess(command):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are an AI assistant named Jarvis skilled in everything like Alexa and Google Cloud. Answer the following request clearly and concisely: {command}"
    
    response = model.generate_content([prompt])
    print(response.text if response else "Sorry, I couldn't process that.")