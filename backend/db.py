import os
import pymssql
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymssql.connect(
        server=os.getenv("DB_SERVER"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=1433,          # Azure SQL default
        login_timeout=10
    )