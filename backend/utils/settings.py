import os
from dotenv import load_dotenv

load_dotenv(override=True)

DEVELOPMENT = os.environ.get("DEVELOPMENT")
