# must install pip install -q -U google-genai

# To run this code you need to install the following dependencies:
# pip install google-genai
import os
import asyncio
import base64
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

app=FastAPI()
client = genai.Client(api_key=api_key)

# Shared state
latest_image = None
latest_label = None
image_event = asyncio.Event()  # event to signal new image

'''
@app.get("/gemini-response/{photo_path}")
def gemini_response(photo_path: str):
    # Access the API key
    with open(photo_path, 'rb') as f:
      image_bytes = f.read()
    
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
    return {"response": response.text}
'''
@app.post("/gemini-response")
async def upload_image(file: UploadFile = File(...)):
    """
    Endpoint for Raspberry Pi to upload an image.
    Processes image with Gemini and updates shared state.
    """
    global latest_image, latest_label

    image_bytes = await file.read()

    # Send to Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type=file.content_type),
            "Tell us if this is recyclable or not. Respond with only 'recyclable' or 'not recyclable'."
        ]
    )

    # Update shared state
    latest_image = image_bytes
    latest_label = response.text.strip()

    # Notify waiting GET requests
    image_event.set()
    image_event.clear()  # reset for next image

    return {"status": "processed", "label": latest_label}

@app.get("/latest-image")
async def get_latest_image():
    """
    Long-poll GET endpoint.
    Waits until a new image is uploaded by the Pi.
    Returns image + label in JSON.
    """
    await image_event.wait()  # wait until a new image is uploaded

    return JSONResponse({
        "label": latest_label,
        "image_base64": base64.b64encode(latest_image).decode()
    })

