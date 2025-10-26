import cv2
import random

cap = cv2.VideoCapture(0)
save_dir = "/home/pi/CamPics/"

# "/home/pi/CamPics/" 
# "/Users/imadshaikh/Desktop/TempPics/"

ret, frame = cap.read()
if ret:
    random_integer = random.randint(0, 1000000)
    filename = save_dir + f"capture-{random_integer}.jpg"
    cv2.imwrite(str(filename), frame)

cap.release()
cv2.destroyAllWindows()