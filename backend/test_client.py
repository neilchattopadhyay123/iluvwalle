import requests
import sys
from pathlib import Path

# Configuration
URL = "http://127.0.0.1:8000/upload"
IMAGE_PATH = Path(__file__).parent / "images" / "metal_can.jpg"  # Test with existing image
print(f"Looking for image at: {IMAGE_PATH.absolute()}")

def test_upload_endpoint():
    if not IMAGE_PATH.exists():
        print(f"Error: Image file not found: {IMAGE_PATH}")
        return False

    with open(IMAGE_PATH, "rb") as image_file:
        files = {"image": (IMAGE_PATH.name, image_file, "image/jpeg")}
        
        try:
            print(f"Sending request to {URL}")
            print(f"Image: {IMAGE_PATH}")
            
            resp = requests.post(URL, files=files, timeout=60)
            print("\nStatus:", resp.status_code)
            
            if resp.status_code == 200:
                result = resp.json()
                print("Success! Response:")
                print(f"Saved as: {result.get('filename')}")
                print(f"Message: {result.get('message')}")
                return True
            else:
                print("Error response:")
                try:
                    print(resp.json())
                except Exception:
                    print(resp.text)
                return False
                
        except requests.exceptions.ConnectionError:
            print("Connection failed. Is the server running?")
            return False
        except Exception as e:
            print(f"Request failed: {e}")
            return False

if __name__ == "__main__":
    success = test_upload_endpoint()
    sys.exit(0 if success else 1)
