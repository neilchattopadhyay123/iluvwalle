# test_upload_real_file.py
from fastapi.testclient import TestClient
from main import app  # change 'main' to your module name if different

client = TestClient(app)

def test_upload_real_image():
    image_path = "metal_can.jpg"  # must exist in the working directory

    with open(image_path, "rb") as f:
        resp = client.post(
            "/upload",
            files={"image": ("metal_can.jpg", f, "image/jpeg")},
        )

    assert resp.status_code == 200, resp.text
    data = resp.json()
    assert "filename" in data and data["filename"].startswith("metal_can")
    assert "message" in data
    print(data)

if __name__ == "__main__":
    test_upload_real_image()
