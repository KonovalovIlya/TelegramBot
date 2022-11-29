from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_city(chat_id):
    """
    Город, где будет проводиться поиск.
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'В каком городе подобрать отель?'
    keyboard.row(
        types.InlineKeyboardButton(text='London', callback_data='London'),
        types.InlineKeyboardButton(text='New York', callback_data='New York'),
        types.InlineKeyboardButton(text='Paris', callback_data='Paris')
    )

    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
