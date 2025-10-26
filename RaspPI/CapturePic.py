import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
save_dir = "/home/pi/CamPics"

# "/home/pi/CamPics" 1
# "/Users/imadshaikh/Desktop/TempPics/"

ret, frame = cap.read()
if ret:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = save_dir + f"capture-{timestamp}.jpg"
    cv2.imwrite(str(filename), frame)

cap.release()
cv2.destroyAllWindows()