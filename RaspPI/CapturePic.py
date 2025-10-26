import cv2
import random
import requests

url = "http://ad.psu.edu:8000/gemini-response"
cap = cv2.VideoCapture(0)
save_dir = "/home/pi/CamPics/"

# "/home/pi/CamPics/" 
# "/Users/imadshaikh/Desktop/TempPics/"

ret, frame = cap.read()
if ret:
    random_integer = random.randint(0, 1000000)
    filename = save_dir + f"capture-{random_integer}.jpg"
    cv2.imwrite(str(filename), frame)

with open(filename, "rb") as f:
    img_data = {"file": f} # raw binary file
response = requests.post(url, files=img_data)

cap.release()
cv2.destroyAllWindows() 

