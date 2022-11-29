from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def help_key_board(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Не забудь отправить коммент автору. Для поиска отелей нажми "Начать поиск"'
    keyboard.row(
        types.InlineKeyboardButton(text='Написать автору', url='telegram.me/AuthorTB'),
        types.InlineKeyboardButton(text='Начать поиск', callback_data='start_search')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
