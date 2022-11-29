from keyboards import get_range_price_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_range_price(chat_id):
    """
    Определяет диапазон цен за номер за ночь
    """

    get_range_price_key_board.get_range_price(chat_id)
