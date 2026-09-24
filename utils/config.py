import os
from dotenv import load_dotenv

load_dotenv()

# Backend URL
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

# Request timeout
REQUEST_TIMEOUT_SECONDS = int(
    os.getenv(
        "REQUEST_TIMEOUT_SECONDS",
        "120"
    )
)