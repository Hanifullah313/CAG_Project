from fastapi import APIRouter, UploadFile, File, HTTPException, Query
import uuid as uuid_pkg
import os 
from src.utils.pdf_processor import extract_text_from_pdf
from src.utils.llm_client import get_llm_response
from src.data_store import data_store  # Import the shared data store

router = APIRouter()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload/{uuid}", status_code=201)
async def upload_pdf(uuid: uuid_pkg.UUID, file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    uuid_str = str(uuid)
    if uuid_str in data_store:
        raise HTTPException(status_code=400, detail="UUID already exists. Use PUT to update the file")

    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")
    
    try:
        # Save file to disk
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Extract text
        extracted_text = extract_text_from_pdf(file_path)
        if not extracted_text:
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF")
        
        # Store in data_store
        data_store[uuid_str] = extracted_text
        return {"uuid": uuid_str, "message": "File uploaded successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@router.put("/update/{uuid_str}")
async def update_pdf(uuid_str: str, file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail="UUID not found")
    
    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")
    
    try:
        # Save file to disk
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Extract text
        new_text = extract_text_from_pdf(file_path)
        if not new_text:
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF")
        
        # Append to existing text
        data_store[uuid_str] += "\n\n" + new_text
        return {"uuid": uuid_str, "message": "File updated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@router.get("/chat/{uuid_str}")
async def chat_with_pdf(uuid_str: str, query: str = Query(..., min_length=1, max_length=500)):
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail="UUID not found")

    stored_text = data_store[uuid_str]
    if not stored_text:
        raise HTTPException(status_code=404, detail="No text extracted from PDF")

    try:
        llm_response = get_llm_response(context=stored_text, query=query)
        return {"uuid": uuid_str, "query": query, "response": llm_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@router.delete("/delete/{uuid_str}", status_code=204)
async def delete_data(uuid_str: str):
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail="UUID not found")
    
    del data_store[uuid_str]
    
    # Delete uploaded files with this UUID
    for filename in os.listdir(UPLOAD_DIR):
        if filename.startswith(uuid_str):
            os.remove(os.path.join(UPLOAD_DIR, filename))
    
    return {"message": "Data deleted successfully"}

@router.get("/listUUIDs", response_model=dict)
async def list_all_uuids():
    return {"uuids": list(data_store.keys())}