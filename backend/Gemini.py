import os
import time
import google.generativeai as genai
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_KEY")

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Debug print to check if API key is loaded (showing only first few characters for security)
print(f"API Key loaded: {GOOGLE_API_KEY[:8]}...")

def get_gemini_response(prompt, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            # Get available models and use the first Gemini model
            models = [m.name for m in genai.list_models()]
            model_name = [m for m in models if 'gemini' in m][0]
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
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

# Example prompt - keep it short for free tier
prompt = "Tell a short tech joke in one sentence"
print("Sending request to Gemini (with rate limit handling)...")
response = get_gemini_response(prompt)
print("\nResponse:", response)