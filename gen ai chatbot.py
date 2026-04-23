import google.generativeai as genai
import os


genai.configure(api_key="AIzaSyCPQ7ujRyuI3TQmaRpm3aagpUI0j805HPo")
model  = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat = model.start_chat(history=[])
print("idealabs chatbot (Type 'exit' to quit)")
print("welcome how can i help you?")

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exist","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"Idealabs:[response.text)")
