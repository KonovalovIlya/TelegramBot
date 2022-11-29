from database.update_user_info import update_user_info
from keyboards import get_amount_key_board, get_city_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def get_amount(chat_id, message=None):
    """
    Определяет количество отелей по которым необходимо собрать информацию
    """
    if message is None:
        get_amount_key_board.get_amount(chat_id)
    else:
        if message.text.isascii():
            update_user_info(('city',), (message.text.join(['''"''', '''"''']),), message.chat.id)
            get_amount_key_board.get_amount(message.chat.id)
        else:
            bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
            get_city_key_board.get_city(message.chat.id)
