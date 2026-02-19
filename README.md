# VastuAI – Image-Based Intelligent Vastu Analyzer 🏛🧠
Using Google Gemini Vision API and a custom Vastu Rule Engine to analyze house floor plans.
## Features
- **Image-Based Analysis**: Upload a floor plan and let AI do the work.
- **Gemini Vision Integration**: Extracts room types and positions with high accuracy.
- **Rule-Based Vastu Engine**: Calculates scores based on traditional Vastu Shastra principles.
- **Interactive UI**: Real-time score meter and improvement suggestions.
## Tech Stack
- **Frontend**: React, Tailwind CSS, Chart.js, Framer Motion
- **Backend**: Flask (Python), Gemini Vision API
- **AI**: Google Gemini 1.5 Flash
## Setup Instructions
### Backend
1. Navigate to the `backend` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your `GEMINI_API_KEY`.
4. Run the server:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to the `frontend` folder.
2. Install dependencies (requires Node.js):
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
## Assumptions
- The top of the uploaded image is assumed to be **North**.
- The analysis is based on generalized Vastu principles.
