# must install pip install -q -U google-genai
from google import genai
from google.genai import types

import PIL.Image

#testing branch push
#test 2 
#implement with database later
image = PIL.Image.open("C:/Users/phone/Downloads/ugly.jpg")

client = genai.Client(api_key="API KEY")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["something", image])

print(response.text)