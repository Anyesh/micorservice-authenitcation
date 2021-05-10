import os
from pathlib import Path

BASEDIR = Path(__file__).parent


class Config:

    # General Config
    FLASK_APP = os.environ.get("FLASK_APP", "app.py")
    FLASK_ENV = os.environ.get("FLASK_ENV", "dev")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", True)
    APP_NAME = os.environ.get("APP_NAME", "Login App")
