📄 PDF Insight AI ✨

Chat with Your Documents – Powered by Google Gemini AI

PDF Insight AI Banner

Transform your static PDF documents into interactive conversational partners. With PDF Insight AI, you can upload documents, ask questions, and receive smart, context-aware answers — all powered by Google’s Gemini AI.
🌟 Project Name

PDF Insight AI
🚀 Features

    🔐 PDF Upload & Management – Upload and manage PDFs with UUID-based tracking

    🤖 AI-Powered Q&A – Ask natural-language questions and receive intelligent answers

    📝 Document Versioning – Easily update existing documents with new content

    🔌 RESTful API – Simple, developer-friendly endpoints for seamless integration

    🌍 Ngrok Support – Tunnel your local server for easy sharing and testing

⚙️ Tech Stack
Layer	Tools
Backend	Python, FastAPI
AI Engine	Google Gemini API
PDF Processing	PyPDF2
Deployment	Uvicorn, Ngrok
Environment	Python 3.10+
🛠️ Installation
1️⃣ Clone the Repository

git clone https://github.com/yourusername/pdf-insight-ai.git
cd pdf-insight-ai

2️⃣ Create and Activate Virtual Environment

# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Create .env File

GOOGLE_API_KEY=your_api_key_here

🚦 Running the Application

Start the development server:

uvicorn main:app --reload

Access the API at:
👉 http://localhost:8000
🌐 API Endpoints
Endpoint	Method	Description
/api/v1/upload/{uuid}	POST	Upload a PDF document
/api/v1/update/{uuid}	PUT	Update an existing PDF
/api/v1/chat/{uuid}	GET	Ask questions about a document
/api/v1/delete/{uuid}	DELETE	Remove a document
/api/v1/listUUIDs	GET	List all uploaded document UUIDs
📖 Example Usage
📤 Upload a PDF

curl -X POST "http://localhost:8000/api/v1/upload/550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"

❓ Ask a Question

curl -X GET "http://localhost:8000/api/v1/chat/550e8400-e29b-41d4-a716-446655440000?query=What%20is%20the%20main%20topic?"

📋 List All Documents

curl -X GET "http://localhost:8000/api/v1/listUUIDs"

📂 Project Structure

pdf-insight-ai/
├── main.py                  # Main application entry point
├── requirements.txt         # Dependencies
├── .env.example             # Environment template
├── src/
│   ├── routers/             # API routes
│   │   └── data_handler.py
│   ├── utils/               # Utility modules
│   │   ├── llm_client.py    # Gemini AI integration
│   │   └── pdf_processor.py # PDF text extraction
│   └── data_store.py        # In-memory document storage
└── uploads/                 # PDF storage directory

🤝 Contributing

We welcome contributions! Follow these steps:

    Fork the repository

    Create a new branch

git checkout -b feature/your-feature-name

Commit your changes

git commit -m "Add your feature"

Push to GitHub

    git push origin feature/your-feature-name

    Open a pull request and get it reviewed 🎉

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
