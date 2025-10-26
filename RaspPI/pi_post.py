import requests 

url = "http://mobile.psu.edu:8000/gemini-response"

with open("phot.jpg", "rb") as f:
    img_data = {"file": f} # raw binary file

response = requests.post(url, files=img_data)

