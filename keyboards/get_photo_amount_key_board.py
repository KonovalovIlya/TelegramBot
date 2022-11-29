from telebot import TeleBot, types
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_photo_amount(chat_id):
    """
    Определяет кол-во фото.
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите кол-во фото.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='photo_1'),
        types.InlineKeyboardButton(text='2', callback_data='photo_2'),
        types.InlineKeyboardButton(text='3', callback_data='photo_3'),
        types.InlineKeyboardButton(text='4', callback_data='photo_4'),
        types.InlineKeyboardButton(text='5', callback_data='photo_5')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)

