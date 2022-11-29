from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_range_distance(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите расстояние от центра в милях.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='dist_1'),
        types.InlineKeyboardButton(text='2', callback_data='dist_2'),
        types.InlineKeyboardButton(text='3', callback_data='dist_3'),
        types.InlineKeyboardButton(text='4', callback_data='dist_4'),
        types.InlineKeyboardButton(text='5', callback_data='dist_5')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
