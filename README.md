# 🌱 Porichorja (পরিচর্যা)

Porichorja is an AI-powered plant disease diagnosis tool. It allows users to upload images of their plants and describe symptoms in Bangla to get instant AI-driven advice.

## 🚀 Features
- **AI-Powered Diagnosis:** Uses advanced vision models to identify plant diseases.
- **Flexible Input:** Works with an image, a text description, or both.
- **Image Preview:** See a thumbnail of the uploaded image before analysis.
- **Side-by-Side UI:** Modern layout for desktop with real-time feedback.

## 🛠 Project Structure
```text
porichorja/
├── backend/
│   ├── ai_engine.py  # Inference logic with Hugging Face Hub
│   └── main.py       # FastAPI server
├── frontend/
│   ├── index.html    # Web UI (Tailwind CSS)
│   └── script.js     # Frontend logic
├── .env              # Environment variables (API Keys)
├── .gitignore        # Ignored files
└── README.md         # Project documentation
```

## ⚙️ Setup Instructions

### Backend
1. Create a `.env` file in the root directory.
2. Add your Hugging Face API token: `HF_TOKEN=your_token_here`.
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn huggingface_hub python-dotenv pillow
   ```
4. Run the backend:
   ```bash
   fastapi dev backend/main.py
   ```

### Frontend
- Open `frontend/index.html` in any modern web browser.

## 📝 Note on Language
Currently, the AI analysis response might be in English due to limited data availability for detailed Bangla botanical terms. Providing responses fully in Bangla is planned for the future.

---
*Developed with 🌱 and AI.*
