from keyboards import get_photo_amount_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def get_photo_amount(chat_id):
    """
    Определяет кол-во фото.
    """
    get_photo_amount_key_board.get_photo_amount(chat_id)
