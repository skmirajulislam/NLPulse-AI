import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or ' '  # Secure the session
    SQLALCHEMY_DATABASE_URI = 'postgresql://db1_owner:OzX4nQUMLV6v@ep-floral-leaf-a182z0z7-pooler.ap-southeast-1.aws.neon.tech/db1?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = os.getenv('PORT') or 8000
