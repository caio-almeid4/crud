import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "mydb",
    user = "postgres",
    password = db_password
)

def connect_db():
    
    conn = psycopg2.connect(
        
        host = "localhost",
        port = 5432,
        database = "mydb",
        user = "postgres",
        password = db_password
    )

    return conn
