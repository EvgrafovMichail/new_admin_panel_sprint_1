"""
There is a file with security settings for Django app
"""

import os


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["127.0.0.1"]


def _show_toolbar_callback(*_) -> bool:
    return DEBUG


SHOW_TOOLBAR_CALLBACK = _show_toolbar_callback
