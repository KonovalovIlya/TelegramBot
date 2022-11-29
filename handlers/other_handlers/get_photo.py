import re
from database.update_user_info import update_user_info
from keyboards import get_photo_key_board
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def get_photo(message):
    """
    Определяет необходимость загрузки фото
    """
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        date = message.text.split(', ')
        update_user_info(
            ('check_in', 'check_out'),
            (date[0].join(['''"''', '''"''']), date[1].join(['''"''', '''"'''])),
            message.chat.id
        )
        get_photo_key_board.get_photo(message.chat.id)
    else:
        bot.send_message(
            message.chat.id,
            'Проверьте указанные даты. Укажите даты въезда и выезда через запятую в формате гггг-мм-дд'
        )
        bot.register_next_step_handler(message, get_photo)

