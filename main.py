from fastapi import FastAPI
# Import FastAPI for creating the API application

from src.routers.data_handler import router
# Import the router containing PDF data handling and chat endpoints

import nest_asyncio
# Import nest_asyncio to allow nested event loops (useful in interactive environments)

from pyngrok import ngrok
# Import pyngrok to expose the local server to the internet

from fastapi.responses import HTMLResponse
# Import HTMLResponse to return HTML content at the root endpoint

from src.routers import data_handler
# Import data_handler module for registering routes

nest_asyncio.apply()
# Apply nest_asyncio to enable nested event loops

ngrok.set_auth_token("30LsyMuYiwST3LIkNGTic8idtUF_3jrNrqPXAsCx54jvTTodi")
# Set ngrok authentication token (ensure this is kept secure)

app = FastAPI(
    title="Chat with PDF API",
    description="Upload PDF, Ask Questions using Gemini API, Update/Delete using UUID",
    version="1.0.0"
)
# Initialize the FastAPI application with metadata

# Register all routes from pdf_router
app.include_router(
     data_handler.router,
     prefix="/api/v1",
     tags=["Data Handling and chat with PDF"])
@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def read_root():
    htmlcontent = """<!DOCTYPE html>
<html>
<head>
    <title>Chat with PDF API</title>
</head>
<body>
    <h1>Welcome to the Chat with PDF API</h1>
    <p>Use the API to upload PDFs and chat with them.</p>
</body>
</html>
"""
    return HTMLResponse(content=htmlcontent , status_code=200 )

if __name__ == "__main__":
    public_url = ngrok.connect(8000)
    print(f"Public URL: {public_url}/docs")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
