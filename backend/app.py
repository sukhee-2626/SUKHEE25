import os
import json
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from vastu_engine import analyze_vastu
from PIL import Image
import io

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    # Use the model that we confirmed working
    model = genai.GenerativeModel('gemini-flash-latest')
else:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")

PROMPT = """
You are an expert in architectural floor plan analysis.

Analyze the uploaded house plan image.

Extract:
1. List of rooms with approximate position (top-left, bottom-right etc.)
2. Identify room type (bedroom, kitchen, toilet, pooja room, hall, entrance)
3. Estimate directional alignment assuming top of image is North.
4. Return structured JSON format only.

Do not explain. Return clean JSON.
Example JSON:
{
  "entrance": "south",
  "kitchen": "north-east",
  "master_bedroom": "south-west",
  "toilet": "north",
  "pooja_room": "east"
}
"""

@app.route('/')
def home():
    try:
        # Serve the professionally structured template
        return render_template('index.html')
    except Exception as e:
        return f"Error loading UI: {str(e)}", 500

@app.route('/analyze', methods=['POST'])
def analyze():
    print("Request received at /analyze")
    if not api_key:
        return jsonify({"error": "API Key not configured on server"}), 500

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    
    img_bytes = file.read()
    print(f"Image received: {len(img_bytes)} bytes")
    img = Image.open(io.BytesIO(img_bytes))
    
    try:
        print("Sending request to Gemini...")
        
        response = model.generate_content([PROMPT, img])
        print("Gemini Response received.")
        # Extract JSON from response
        raw_text = response.text
        print(f"Raw Gemini Text: {raw_text}")
        

        # Helper to clean JSON string
        def clean_json(text):
            if "```json" in text:
                try:
                    text = text.split("```json")[1].split("```")[0]
                except IndexError:
                    pass
            elif "```" in text:
                try:
                    text = text.split("```")[1].split("```")[0]
                except IndexError:
                    pass
            return text.strip()

        cleaned_text = clean_json(raw_text)
        print(f"Cleaned JSON Text: {cleaned_text}")
        
        try:
            data = json.loads(cleaned_text)
        except json.JSONDecodeError as je:
            print(f"JSON Decode Error: {je}")
            # Fallback: try to repair common JSON issues or return error
            return jsonify({"error": f"AI response was not valid JSON: {str(je)}"}), 500
        
        # Analyze Vastu using the engine
        analysis = analyze_vastu(data)
        
        return jsonify({
            "raw_data": data,
            "analysis": analysis
        })
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        
        # Check for quota exceeded error (429)
        if "429" in str(e) or "quota" in str(e).lower():
            # Return a specific error code for quota issues
            return jsonify({
                "error": "API Quota Exceeded. Please try again in a minute.",
                "details": "The free tier limit for the AI model has been reached."
            }), 429
            
        # Fallback for demo if API fails or quota exceeded
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "api_key_set": bool(api_key), "model": "gemini-flash-latest"})

if __name__ == '__main__':
    print("VastuAI Backend Running on http://localhost:5000")
    app.run(debug=True, port=5000)
