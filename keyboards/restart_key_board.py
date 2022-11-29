from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def restart(chat_id):
    '''
    Запускает новый поиск
    '''
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Для нового поиска нажми "Начать поиск"'
    keyboard.row(
        types.InlineKeyboardButton(text='Начать поиск', callback_data='start_search')
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
