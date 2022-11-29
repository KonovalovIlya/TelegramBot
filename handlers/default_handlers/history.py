from database.get_user_data import get_user_data
from telebot import TeleBot
from config_data import config

bot = TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(commands=['history'])
def history(chat_id):
    '''
    История запросов.
    '''

    res = get_user_data(chat_id)
    bot.send_document(chat_id, open(res[1], 'rb'))
