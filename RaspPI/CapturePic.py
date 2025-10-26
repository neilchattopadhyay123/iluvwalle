import cv2
from datetime import datetime
from pathlib import Path

cap = cv2.VideoCapture(0)
save_dir = Path("/USERS/imadshaikh/Desktop/TempPics")
save_dir.mkdir(parents=True, exist_ok=True)

ret, frame = cap.read()
if ret:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = save_dir / f"capture-{timestamp}.jpg"
    cv2.imwrite(str(filename), frame)

cap.release()
cv2.destroyAllWindows()