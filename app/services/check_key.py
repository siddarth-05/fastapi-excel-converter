from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def verify(received_key: str) -> bool:
    """Verify if the received parameter matches the configured API key."""
    return received_key == API_KEY

# Alias to support different naming preferences
check_key = verify