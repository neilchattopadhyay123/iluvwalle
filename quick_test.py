import requests
from pathlib import Path

image_path = Path(__file__).parent / "backend" / "images" / "metal_can.jpg"
print(f"Uploading image from: {image_path}")

with open(image_path, "rb") as f:
    response = requests.post(
        "http://localhost:8000/upload",
        files={"image": f}
    )
    print("\nResponse:", response.status_code)
    print(response.json())