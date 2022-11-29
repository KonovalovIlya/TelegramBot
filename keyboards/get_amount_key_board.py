from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_amount(chat_id):
    """
    Определяет количество отелей по которым необходимо собрать информацию
    """

    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите кол-во отелей.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='amount_1'),
        types.InlineKeyboardButton(text='2', callback_data='amount_2'),
        types.InlineKeyboardButton(text='3', callback_data='amount_3'),
        types.InlineKeyboardButton(text='4', callback_data='amount_4'),
        types.InlineKeyboardButton(text='5', callback_data='amount_5')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
