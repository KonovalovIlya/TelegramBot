from telebot import TeleBot
import sqlite3 as db


import database.get_user_data
from config_data import config
from handlers import default_handlers, other_handlers
from utils.cbw import callback_worker
# from keyboards.get_city_key_board import callback_worker as cws


bot = TeleBot(token=config.BOT_TOKEN)

bot.message_handler(commands=config.DEFAULT_COMMANDS[0])(default_handlers.start.welcome)
bot.message_handler(commands=config.DEFAULT_COMMANDS[1])(default_handlers.help.help_message)
bot.message_handler(commands=config.DEFAULT_COMMANDS[2])(default_handlers.history.history)

bot.message_handler(content_types=['text'])(other_handlers.get_photo.get_photo)
bot.callback_query_handler(func=lambda call: True)(callback_worker)
# bot.callback_query_handler(func=lambda call: True)(cws)

# if __name__ == '__main__':
#     pass