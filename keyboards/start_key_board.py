from database import create_user, update_user_info
from telebot import types, TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def start_key_board(chat_id, data=None ):
    '''
    Вызывает клавиатуру выбора команд
    '''
    create_user.create_user(chat_id)
    update_user_info.update_user_info(('logfile',), (str(chat_id).join(['"log_', '.txt"']),), chat_id)
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Могу найти отели:'
    keyboard.row(
        types.InlineKeyboardButton(text='Дешовые', callback_data='/lowprice'),
        types.InlineKeyboardButton(text='Дорогие', callback_data='/highprice'),
        types.InlineKeyboardButton(text='Для вас', callback_data='/bestdeal')
    )
    keyboard.row(
        types.InlineKeyboardButton(text='Help', callback_data='/help'),
        types.InlineKeyboardButton(text='History', callback_data='/history'),
    )
    bot.send_message(chat_id, text=key_message, reply_markup=keyboard)
