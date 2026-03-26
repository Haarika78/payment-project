import sqlite3

def get_db():
    conn = sqlite3.connect("payments.db")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            status TEXT
        )
    """)
    
    conn.commit()
    conn.close()