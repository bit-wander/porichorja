# 🌱 Porichorja (পরিচর্যা)

Porichorja is an AI-powered plant disease diagnosis tool. It allows users to upload images of their plants and describe symptoms in Bangla to get instant AI-driven advice.

## 🚀 Features
- **Expert Query System:** Discuss agricultural queries and get expert advice.
- **RAG Powered:** Uses reliable agricultural data for accurate responses.
- **Flexible Input:** Currently supports text-based queries in Bangla.
- **Side-by-Side UI:** Modern layout for seamless interaction.

### Demonstration
![Demonstration](assets/demonstration.gif)

### Desktop View
![Desktop UI](docs/desktop_ui.png)

### Mobile View
![Mobile UI](docs/mobile_ui.png)

## 🛠 Project Structure
```text
porichorja/
├── assets/           # Project assets (images, gifs)
├── backend/
│   ├── data/         # RAG data files (embeddings, index, CSV)
│   ├── ai_engine.py  # Inference logic with Ollama
│   └── main.py       # FastAPI server
├── frontend/
│   ├── index.html    # Web UI (Tailwind CSS)
│   └── script.js     # Frontend logic
├── .env              # Environment variables (API Keys)
├── .gitignore        # Ignored files
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## ⚙️ Setup Instructions

### Backend
1. Create a `.env` file in the root directory.
2. Add your Ollama API key: `OLLAMA_API_KEY=your_key_here`.
3. (Optional) Add your Hugging Face token if using HF models: `HF_TOKEN=your_token_here`.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the backend:
   ```bash
   fastapi dev backend/main.py
   ```

### Frontend
- Open `frontend/index.html` in any modern web browser.

---
*Developed with 🌱 and AI.*
