from dotenv import load_dotenv
import os

# Try to load from .env file
load_dotenv()

# Print all environment variables
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value if 'KEY' not in key else '***'}")