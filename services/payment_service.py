from database.db import get_db

class DummySession:
    def __init__(self):
        self.url = "/success"

def create_checkout_session():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO transactions (amount, status) VALUES (?, ?)",
        (500, "SUCCESS")
    )
    
    conn.commit()
    conn.close()

    return DummySession()
