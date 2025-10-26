import cv2
import random
import requests
import os
import time

url = "http://104.39.73.209:8000/gemini-response"
save_dir = "/Users/imadshaikh/Desktop/TempPics/"
os.makedirs(save_dir, exist_ok=True)

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