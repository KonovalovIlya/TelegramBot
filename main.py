from telebot.types import Message
from loader import bot
from utils.set_bot_commands import set_default_commands
from database.create_db import create_db
from handlers.default_handlers.start import welcome
from utils.cbw import callback_worker



if __name__ == '__main__':
    set_default_commands(bot)
    create_db()
    # callback_worker()
    bot.polling(non_stop=True)

