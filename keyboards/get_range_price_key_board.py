from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_range_price(chat_id):
    """
    Определяет диапазон цен за номер за ночь
    """

    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите стоимость номера за ночь в $'
    keyboard.row(
        types.InlineKeyboardButton(text='До 25', callback_data='0, 25'),
        types.InlineKeyboardButton(text='От 25 до 75', callback_data='25, 75'),
        types.InlineKeyboardButton(text='От 75 до 150', callback_data='75, 150'),
    )
    keyboard.row(
        types.InlineKeyboardButton(text='От 150 до 250', callback_data='150, 250'),
        types.InlineKeyboardButton(text='От 250 до 500', callback_data='250, 500')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
