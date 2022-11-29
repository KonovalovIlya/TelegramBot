from handlers.other_handlers.get_photo import get_photo
from telebot import TeleBot
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_date(message):
    """
    Определяет период заселения
    """
    bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
    bot.register_next_step_handler(message, get_photo)

