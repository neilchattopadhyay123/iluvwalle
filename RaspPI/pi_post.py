import requests, base64

url = 

with open("phot.jpg", "rb") as f:
    img_data = {"file": f} # raw binary file

response = requests.post(url, files=img_data)

print(response.json()) #"url_to_your_endpoint"
