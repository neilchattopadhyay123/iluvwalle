import cv2
import random
import requests
import os
import time

url = "http://104.39.73.209:8000/gemini-response"
cap = cv2.VideoCapture(0)
save_dir = "/Users/imadshaikh/Desktop/TempPics/"
os.makedirs(save_dir, exist_ok=True)

# "/home/pi/CamPics/" 
# "/Users/imadshaikh/Desktop/TempPics/"

# --- Warm up the camera ---
print("Warming up camera...")
time.sleep(2)  # Wait 2 seconds for camera to adjust (you can tweak this)
for i in range(5):  # Read and discard first few frames
    cap.read()

# --- Capture the image ---
ret, frame = cap.read()
if ret:
    random_integer = random.randint(0, 1000000)
    filename = os.path.join(save_dir, f"capture-{random_integer}.jpg")
    cv2.imwrite(filename, frame)
    print(f"Captured image: {filename}")

    # --- Send image to server ---
    with open(filename, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        print(f"Server responded with: {response.status_code}")
        print(response.text)
else:
    print(" Failed to capture image")

cap.release()
cv2.destroyAllWindows()