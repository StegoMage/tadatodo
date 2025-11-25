import psycopg2
import psycopg2.extras
import os

DB_CONFIG = {
    "dbname": "tadatodo",
    "user": "postgres",
    "password": "MiniBeast",
    "host": "localhost",
    "port": 5432
}



def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
