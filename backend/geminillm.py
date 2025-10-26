# must install pip install -q -U google-genai

# To run this code you need to install the following dependencies:
# pip install google-genai
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

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


