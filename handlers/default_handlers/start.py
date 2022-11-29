from telebot.types import Message
from database import create_user, update_user_info
from keyboards.start_key_board import start_key_board

from telebot import TeleBot
from config_data import config

bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    '''
    Приветствует пользователя
    '''

    create_user.create_user(message.chat.id)
    update_user_info.update_user_info(('logfile',), (str(message.chat.id).join(['"log_', '.txt"']),), message.chat.id)

    bot.send_message(message.chat.id,
                     'Привет, {name}!\nНе знаешь с чего начать?\nХочешь узнать что я могу?\nНажми кнопку Help. '
                     'Или выбери другую команду.'.format(name=message.from_user.first_name))
    start_key_board(message.chat.id)
