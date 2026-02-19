import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

try:
    print("\nAttempting generation with gemini-flash-latest...")
    model = genai.GenerativeModel('gemini-flash-latest')
    response = model.generate_content("Hello")
    print("SUCCESS! gemini-flash-latest IS WORKING!")
except Exception as e:
    print(f"gemini-flash-latest failed: {str(e)}")
    
    try:
        print("\nAttempting generation with gemini-pro-latest...")
        model = genai.GenerativeModel('gemini-pro-latest')
        response = model.generate_content("Hello")
        print("SUCCESS! gemini-pro-latest IS WORKING!")
    except Exception as e:
        print(f"gemini-pro-latest failed: {str(e)}")
