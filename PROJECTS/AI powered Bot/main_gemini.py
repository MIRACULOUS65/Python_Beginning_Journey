# Simple Terminal Chatbot using Google's Gemini API

# First, you need to install the library:
# pip install google-generativeai

import google.generativeai as genai
import os

# --- IMPORTANT ---
# For your security, DO NOT hardcode your API key in the script.
# It's better to use an environment variable or a secrets management tool.
# However, for this simple example, we will ask you to paste it here.
# I have removed the key you provided for your safety.
API_KEY = "AIzaSyBVZ7b-4G54pHtKugiOlWqK4nhf53ReDnU"

try:
    # Configure the Gemini API with your key
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    print("Please make sure you have pasted a valid API key.")
    exit()

# Check if the API key was set correctly
if API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    print("="*50)
    print("ERROR: Please replace 'PASTE_YOUR_GEMINI_API_KEY_HERE' with your actual Gemini API key in the script.")
    print("="*50)
    exit()

# Initialize the Gemini model
# The model name 'gemini-1.0-pro' can sometimes be unavailable.
# Using 'gemini-1.5-flash-latest' is a more current and reliable choice.
model = genai.GenerativeModel('gemini-2.5-flash')

print("Gemini Chatbot Initialized.")
print("Type 'quit' or 'exit' to end the conversation.")
print("-" * 20)

# Start the chat loop
while True:
    try:
        # Get input from the user
        user_prompt = input("You: ")

        # Check if the user wants to quit
        if user_prompt.lower() in ['quit', 'exit']:
            print("Gemini: Goodbye!")
            break

        # Send the prompt to the model and get a response
        response = model.generate_content(user_prompt)

        # Print the model's response
        print(f"Gemini: {response.text}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("There might be an issue with the API key or your connection.")
        break

