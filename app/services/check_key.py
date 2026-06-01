from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("API_KEY")
def is_valid_api_key(passed_key):
    if key == passed_key:
        return True
    else:
        return False

# print(key)