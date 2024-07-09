# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    # SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')