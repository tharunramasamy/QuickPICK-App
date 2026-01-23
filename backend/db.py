import os
import pymssql
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = pymssql.connect(
            server=os.getenv("DB_SERVER"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=1433,
            login_timeout=10,
            timeout=10
        )
        return conn
    except Exception as e:
        print("DB connection failed:", e)
        raise