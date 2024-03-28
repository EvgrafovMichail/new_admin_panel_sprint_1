import os

from pathlib import Path

from split_settings.tools import include
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
include(
    os.path.join(".", "components", "security.py"),
    os.path.join(".", "components", "app_definition.py"),
    os.path.join(".", "components", "database.py"),
    os.path.join(".", "components", "auth.py"),
    os.path.join(".", "components", "internationalization.py"),
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
