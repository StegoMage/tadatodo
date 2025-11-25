import psycopg2
import psycopg2.extras

DB_CONFIG = {
    "dbname": "tadatodo",
    "user": "postgres",
    "password": "MiniBeast",
    "host": "localhost",
    "port": 5432
}


def get_db():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            is_complete BOOLEAN DEFAULT FALSE
            );                      
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialised!")

