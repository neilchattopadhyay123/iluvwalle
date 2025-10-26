import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import uvicorn
from google import genai
from google.genai import types
from dotenv import load_dotenv

app = FastAPI(
    title="Image Storage API",
    description="API for storing images in the backend/images folder",
    version="1.0.0"
)

# Ensure images directory exists
IMAGES_DIR = Path(__file__).parent / "images"
IMAGES_DIR.mkdir(exist_ok=True)

@app.post("/upload", 
    summary="Upload an image to store",
    response_model=dict,
    tags=["Storage"]
)
async def upload_image(
    image: UploadFile = File(..., description="Image file to store")
):
    """
    Upload and store an image in the backend/images folder.
    
    - Supports common image formats (jpg, png, etc.)
    - Returns the saved image filename
    """
    print(f"Received upload request for file: {image.filename}")  # Debug logging
    if not image:
        return JSONResponse(
            status_code=400,
            content={"error": "Please provide an image file."}
        )

    # Generate safe filename and save path
    filename = Path(image.filename)
    safe_filename = ''.join(c for c in filename.stem if c.isalnum() or c in '-_') + filename.suffix
    save_path = IMAGES_DIR / safe_filename

    # Ensure unique filename
    counter = 1
    while save_path.exists():
        new_filename = f"{Path(safe_filename).stem}_{counter}{filename.suffix}"
        save_path = IMAGES_DIR / new_filename
        counter += 1

    try:
        # Save the uploaded image
        with save_path.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        return {
            "filename": save_path.name,
            "message": f"Image saved successfully to images/{save_path.name}"
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to save image: {str(e)}"}
        )

# must install pip install -q -U google-genai

# To run this code you need to install the following dependencies:
# pip install google-genai

# Load .env file
load_dotenv()

# Access the API key
api_key = os.environ.get("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

with open('backend/images/watterbottle1.png', 'rb') as f:
      image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'tell us if this is recyclable or not? respond with only recyclable or not recyclable.'
    ]
  )

print(response.text)
if __name__ == "__main__":
    # For local testing only. In production use a proper ASGI server.
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
