import os

from dotenv import load_dotenv


load_dotenv()

DB_CONFIG = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "8000")),
    "options": os.environ.get("OPTIONS", ""),
}

SQLITE_PATH = os.environ.get("SQLITE_PATH")

BATCH_SIZE = 100
