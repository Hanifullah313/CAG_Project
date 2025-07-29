PDF Insight AI ✨

https://via.placeholder.com/1200x400?text=PDF+Insight+AI+-+Chat+with+Your+Documents

Transform your PDF documents into conversational partners - PDF Insight AI allows you to upload documents, ask questions, and get intelligent answers powered by Google's Gemini AI.
🌟 Project Name: PDF Insight AI
🚀 Features

    PDF Upload & Management: Securely upload and manage PDF documents with UUID tracking

    AI-Powered Q&A: Ask questions about your documents and get instant answers

    Document Versioning: Update existing documents with new content

    Simple API: Easy-to-use RESTful endpoints for integration

    Ngrok Support: Built-in tunneling for easy testing and sharing

⚙️ Tech Stack

    Backend: Python, FastAPI

    AI: Google Gemini API

    PDF Processing: PyPDF2

    Deployment: Uvicorn, Ngrok

    Environment: Python 3.10+

🛠️ Installation

    Clone the repository:

bash

git clone https://github.com/yourusername/pdf-insight-ai.git
cd pdf-insight-ai

    Create and activate virtual environment:

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

    Install dependencies:

bash

pip install -r requirements.txt

    Create .env file:

env

GOOGLE_API_KEY=your_api_key_here

🚦 Running the Application

Start the development server:
bash

uvicorn main:app --reload

Access the API at http://localhost:8000
🌐 API Endpoints
Endpoint	Method	Description
/api/v1/upload/{uuid}	POST	Upload a PDF document
/api/v1/update/{uuid}	PUT	Update an existing PDF
/api/v1/chat/{uuid}	GET	Ask questions about a document
/api/v1/delete/{uuid}	DELETE	Remove a document
/api/v1/listUUIDs	GET	List all document UUIDs
📖 Example Usage
Upload a PDF
bash

curl -X POST "http://localhost:8000/api/v1/upload/550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"

Ask a Question
bash

curl -X GET "http://localhost:8000/api/v1/chat/550e8400-e29b-41d4-a716-446655440000?query=What%20is%20the%20main%20topic?"

List All Documents
bash

curl -X GET "http://localhost:8000/api/v1/listUUIDs"

📂 Project Structure
text

pdf-insight-ai/
├── main.py                  # Main application entry point
├── requirements.txt         # Dependencies
├── .env.example             # Environment template
├── src/
│   ├── routers/             # API endpoints
│   │   └── data_handler.py
│   ├── utils/               # Utility functions
│   │   ├── llm_client.py    # Gemini AI integration
│   │   └── pdf_processor.py # PDF text extraction
│   └── data_store.py        # Document storage
└── uploads/                 # PDF storage directory

🤝 Contributing

We welcome contributions! Please follow these steps:

    Fork the repository

    Create your feature branch (git checkout -b feature/amazing-feature)

    Commit your changes (git commit -m 'Add some amazing feature')

    Push to the branch (git push origin feature/amazing-feature)

    Open a pull request

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.