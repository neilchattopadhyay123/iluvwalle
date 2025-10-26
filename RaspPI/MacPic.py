import cv2
import random
import requests
import os

url = "http://104.39.73.209:8000/gemini-response"
cap = cv2.VideoCapture(0)
save_dir = "/Users/imadshaikh/Desktop/TempPics/"

# Make sure save_dir exists
os.makedirs(save_dir, exist_ok=True)

ret, frame = cap.read()
if ret:
    random_integer = random.randint(0, 1000000)
    filename = os.path.join(save_dir, f"capture-{random_integer}.jpg")
    cv2.imwrite(filename, frame)

    with open(filename, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        print(f"Server responded with: {response.status_code}")
        print(response.text)

cap.release()
cv2.destroyAllWindows()