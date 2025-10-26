import os
import time
import PIL.Image
import google.generativeai as genai
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# Debug print to check if API key is loaded (showing only first few characters for security)
print(f"API Key loaded: {GOOGLE_API_KEY[:8]}...")

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(prompt, image_path=None, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            contents = []
            
            # Add the text prompt
            contents.append(prompt)
            
            # If image is provided, add it to contents
            if image_path:
                try:
                    image = PIL.Image.open(image_path)
                    contents.append(image)
                    print(f"Image loaded successfully from: {image_path}")
                except Exception as img_error:
                    return f"Error loading image: {str(img_error)}"

            # Use the correct model name for vision tasks
            model_name = 'models/gemini-2.5-flash-image' if image_path else 'models/gemini-2.5-pro'
            model = genai.GenerativeModel(model_name)
            print(f"Using model: {model_name}")
            
            response = model.generate_content(contents=contents)
            return response.text
        except Exception as e:
            error_str = str(e)
            if "429" in error_str:  # Rate limit error
                retry_time = delay * (attempt + 1)  # Exponential backoff
                print(f"Rate limit reached. Waiting {retry_time} seconds before retrying...")
                time.sleep(retry_time)
                continue
            return f"An error occurred: {error_str}"
    return "Maximum retries reached. Please try again later."

# Example prompt with image analysis
if __name__ == "__main__":
    # Example prompt with image analysis (runs only when executed directly)
    prompt = (
        "Answer with one word, categorize the object in the image into either glass, metal,"
        " paper, plastic, or food waste. If it fits none of the categories, say trash."
    )
    image_path = "backend/bottle-water-that-is-half-empty_871349-6225.jpg"
    print("Sending request to Gemini (with rate limit handling)...")
    response = get_gemini_response(prompt, image_path)
    print("\nResponse:", response)