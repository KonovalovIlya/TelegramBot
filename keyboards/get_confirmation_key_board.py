from telebot import TeleBot, types
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


def get_confirmation(data, chat_id):
    """
    Проверка запрашиваемых даных.
    """

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
    keyboard.add(key_no)
    info_all = 'Ищем {amount} отелей в городе {city} с {photo_amount} фото'.format(
        amount=data[6],
        city=data[3],
        photo_amount=data[7]
    )
    bot.send_message(chat_id, text=info_all, reply_markup=keyboard)

