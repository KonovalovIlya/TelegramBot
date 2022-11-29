import sqlite3 as db
from typing import Tuple


def get_user_data(chat_id: int) -> Tuple:
    with db.connect('bot_db') as c:
        cursor = c.cursor()
        return cursor.execute('SELECT * FROM USERS WHERE chat_id={}'.format(chat_id)).fetchone()
