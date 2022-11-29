import sqlite3 as db


def delete_user_data(chat_id: int) -> None:
    with db.connect('bot_db') as c:
        cursor = c.cursor()
        cursor.execute('DELETE FROM USERS WHERE chat_id={}'.format(chat_id))
