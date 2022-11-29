from keyboards import get_city_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_city(chat_id):
    """
    Город, где будет проводиться поиск.
    """
    get_city_key_board.get_city(chat_id)

