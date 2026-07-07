import sqlite3


def create_database():
    conn = sqlite3.connect("messages.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        message TEXT,
        date TEXT,
        time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_message(phone, message, date, time, status):
    conn = sqlite3.connect("messages.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO messages(phone, message, date, time, status)
    VALUES (?, ?, ?, ?, ?)
    """, (phone, message, date, time, status))

    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()

    conn.close()
    return data 
def update_status(phone, status):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE messages
                   SET status = ?
                   WHERE phone = ?
                   """, (status, phone))
    conn.commit()
    conn.close()
def delete_message(message_id):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE id=?",
        (message_id,)
    )

    conn.commit()
    conn.close()    
def edit_message(message_id, new_message):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE messages
        SET message = ?
        WHERE id = ?
        """,
        (new_message, message_id)
    )

    conn.commit()
    conn.close()    
