import sqlite3 as db
from sqlite3 import Error


def create_user(chat_id: int) -> None:
    with db.connect('bot_db') as connection:
        cursor = connection.cursor()
        try:
            cursor.executescript(f'''INSERT INTO USERS (chat_id) VALUES({chat_id});''')
        except Error:
            cursor.executescript(f'''UPDATE USERS SET chat_id=({chat_id});''')
        connection.commit()
