import sqlite3 as db
from sqlite3 import Error
from typing import Tuple


def update_user_info(fields: Tuple, values: Tuple, chat_id: int) -> None:
    with db.connect('bot_db') as connection:
        cursor = connection.cursor()
        parameter = ', '.join('='.join([j, values[i]]) for i, j in enumerate(fields))
        try:
            cursor.execute('UPDATE USERS SET {} WHERE chat_id = {}'.format(parameter, chat_id))
        except Error:
            print(Error('Ошибка'))
        connection.commit()
