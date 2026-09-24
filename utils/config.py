import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

REQUEST_TIMEOUT_SECONDS = int(
    os.getenv(
        "REQUEST_TIMEOUT_SECONDS",
        "120"
    )
)