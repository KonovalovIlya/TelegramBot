from database import get_user_data
from keyboards import get_confirmation_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_confirmation(chat_id):
    """
    Проверка запрашиваемых даных.
    """

    res = get_user_data.get_user_data(chat_id)
    get_confirmation_key_board.get_confirmation(res, chat_id)
