from keyboards.help_key_board import help_key_board
from telebot import TeleBot
from config_data import config

bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(commands=['help'])
def help_message(chat_id):
    '''
    Выводит описание возможностей бота
    '''

    help_message_str = 'Я могу подбирать отели.\nЕсли нажмешь на кнопку "Дешовые", я подберу самые дешовые отели.\n'\
        'Если нажмешь на кнопку "Дорогие", я подберу самые дорогие отели.\nЕсли нажмешь на кнопку "Для вас", '\
        'я подберу самые подходящие отели под указанные параметры.\nЕсли нажмешь на кнопку "History", я отправлю '\
        'тебе файл с ответами на все запросы которые ты мне отправлял.\n'
    bot.send_message(chat_id, help_message_str)

    help_key_board(chat_id)
