from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_photo(chat_id):
    """
    Определяет необходимость загрузки фото
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Загрузить фото по отелям?'
    keyboard.row(
        types.InlineKeyboardButton(text='Да', callback_data='yes_p'),
        types.InlineKeyboardButton(text='Нет', callback_data='no_p')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
