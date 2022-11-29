import sqlite3 as db


def create_db():
    with db.connect('bot_db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS (chat_id INTEGER UNIQUE ON CONFLICT ROLLBACK, logfile TEXT, command TEXT, city TEXT, range_price TEXT, 
            range_distance TEXT, amount TEXT, photo_amount TEXT, check_in TEXT, check_out TEXT)
        ''')
