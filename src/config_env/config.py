import os
from dotenv import load_dotenv
load_dotenv() 

class Config:
    MYSQL_DB_USER = os.getenv('MYSQL_DB_USER')
    MYSQL_DB_PASSWORD = os.getenv('MYSQL_DB_PASSWORD')
    MYSQL_DB_HOST = os.getenv('MYSQL_DB_HOST')
    MYSQL_DB_PORT = os.getenv('MYSQL_DB_PORT')
    MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME')
    JWT_SECRET = os.getenv('JWT_SECRET')

