# must install pip install -q -U google-genai

# To run this code you need to install the following dependencies:
# pip install google-genai
import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv


# Load image
#image_path = "C:/Users/phone/Downloads/metal_can.jpg"
#image = Image.open(image_path)
#buffered = io.BytesIO()
#image.save(buffered, format="PNG")
#img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

# Load .env file
load_dotenv()

# Access the API key
api_key = os.environ.get("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

# Upload image file
my_file = client.files.upload(file="C:/Users/phone/Downloads/watterbottle1.png")

response = client.models.generate_content(
    model = "gemini-2.5-pro",
    contents=[my_file, "is the item in the photo a recyclable item or not? The only response can be either 'recyclable' or 'not recyclable'." ],
)

print(response.text)

