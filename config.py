import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or ' '  # Secure the session
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = os.getenv('PORT') or 8000
