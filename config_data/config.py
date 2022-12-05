import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
HEADERS = dict()
for _ in os.getenv('HEADERS').split(','):
    HEADERS[_.split(':')[0]] = _.split(':')[1]
URLS = os.getenv('URLS').strip("'[]'").split(', ')

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('history', "Показать историю запросов"),

)
