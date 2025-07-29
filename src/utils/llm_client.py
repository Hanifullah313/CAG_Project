import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(context: str, query: str) -> str:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it in your .env file")
    
    # Configure the API key
    genai.configure(api_key=api_key)
    
    # Use the correct model name for v1beta API
    # Try different model names until one works
    model_names = [
        'gemini-pro',              # Original model name
        'models/gemini-pro',        # Fully qualified name
        'gemini-1.0-pro',           # Newer naming
        'models/gemini-1.0-pro',    # Fully qualified newer name
        'gemini-1.5-flash',         # Latest flash model
        'gemini-1.5-pro-latest'     # Latest pro model
    ]
    
    model = None
    for model_name in model_names:
        try:
            model = genai.GenerativeModel(model_name)
            # Test with a small prompt to verify it works
            test_response = model.generate_content("Hello")
            if test_response.text:
                break  # Stop when we find a working model
        except Exception:
            model = None
    
    if model is None:
        raise Exception("Could not find a working Gemini model. Please check available models.")
    
    # Create the prompt with context and query
    prompt = f"""
    You are a helpful assistant that answers questions based strictly on the provided context.
    
    CONTEXT:
    {context}
    
    QUESTION: {query}
    
    ANSWER:
    """
    
    # Generate content
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Provide detailed error message
        error_msg = (
            f"LLM Error: {str(e)}\n"
            f"Model: {model_name}\n"
            f"API Version: {genai.__version__}"
        )
        raise Exception(error_msg)