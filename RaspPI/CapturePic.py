import cv2
import random
import requests
import os
import time

# Ensure script runs from its own directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = "http://10.32.121.148:8000/gemini-response"
save_dir = "/home/pi/CamPics/"
os.makedirs(save_dir, exist_ok=True)

# Ensure OpenCV can open GUI
os.environ["DISPLAY"] = ":0"

# "/home/pi/CamPics/" 
# "/Users/imadshaikh/Desktop/TempPics/"

cap = cv2.VideoCapture(0)

print("📸 Camera ready! Press SPACE to capture, or ESC to quit.")
time.sleep(2)  # warm-up delay

while True:
    # Show live camera feed
    ret, frame = cap.read()
    if not ret:
        print("Failed to read from camera.")
        break

    cv2.imshow("Live Feed - Press SPACE to capture", frame)
    key = cv2.waitKey(1) & 0xFF

    # SPACEBAR pressed
    if key == 32:  # ASCII for space
        print("📷 Taking picture...")
        random_integer = random.randint(0, 1000000)
        filename = os.path.join(save_dir, f"capture-{random_integer}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Saved: {filename}")

        # Send image to server
        with open(filename, "rb") as f:
            files = {"file": f}
            try:
                response = requests.post(url, files=files, timeout=10)
                print(f"Server responded: {response.status_code}")
                print(response.text)
            except Exception as e:
                print(f"Upload failed: {e}")

    # ESC key pressed → quit
    elif key == 27:  # ESC
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()