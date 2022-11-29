from keyboards import get_range_distance_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_range_distance(chat_id):
    """
    Определяет максимальное расстояние от центра
    """

    get_range_distance_key_board.get_range_distance(chat_id)
