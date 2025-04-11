import pyautogui
import time
import pyperclip
import google.generativeai as genai
genai.configure(api_key="your api")

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1315, 1051)
temp=0
time.sleep(1)  # Wait for 1 second to ensure the click is registered
while (temp==0):
    temp+=1  
    time.sleep(1)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(680,265)
    time.sleep(0.5)

    pyautogui.dragTo(1850, 898, duration=2.0, button='left')  # Drag for 1 second
    time.sleep(0.5)
   
    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    pyautogui.click(690,270)


    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()
    time.sleep(0.5)

    # Print the copied text to verify
    print("printing")
    print(chat_history)
    # print(is_last_message_from_sender(chat_history))
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use "gemini-1.5-pro" if needed
    prompt = f"""You are Rishabh, a friendly and engaging individual from India who speaks both Hindi and English. You analyze chat history and respond naturally in Hinglish, maintaining a conversational and engaging tone.  

    Guidelines:
    - Respond as Rishabh, keeping the tone friendly and casual.  
    - Use Hinglish (a mix of Hindi and English) naturally in your response and try to give a medium size response.  
    - Do NOT include timestamps or unnecessary formatting—only the next chat response as plain text.  

    Chat History: 
    {chat_history}  

    Now generate Rishabh’s next response:
    """

    
    response = model.generate_content([prompt])

    pyperclip.copy("")
    pyperclip.copy(response.text)
    pyautogui.click(865, 954)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(1840, 954)
   
        # response = completion.choices[0].message.content
        # pyperclip.copy(response)

        # # Step 5: Click at coordinates (1808, 1328)
        # pyautogui.click(1808, 1328)
        # time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # # Step 6: Paste the text
        # pyautogui.hotkey('ctrl', 'v')
        # time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # # Step 7: Press Enter
        # pyautogui.press('enter')
