import re

from telebot import TeleBot
from database import create_user, get_user_data, update_user_info, delete_user_data
from handlers.default_handlers import *
from handlers.other_handlers import *
from keyboards import *
from utils import parsing
from config_data import config


bot = TeleBot(token=config.BOT_TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    chat_id = call.message.chat.id
    if call.data == "/help":
        bot.answer_callback_query(call.id)
        help.help_message(chat_id)

    elif call.data == "/history":
        bot.answer_callback_query(call.id)
        history.history(chat_id)
    else:
        bot.send_message(chat_id, 'Ok')

        if call.data == "/lowprice":
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('command',), ('"lowprice"',), chat_id)
            get_city.get_city(chat_id)

        elif call.data == 'start_search':
            bot.answer_callback_query(call.id)
            create_user.create_user(chat_id)
            start_key_board.start_key_board(chat_id)

        elif call.data == "/highprice":
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('command',), ('"highprice"',), chat_id)
            get_city.get_city(chat_id)

        elif call.data == "/bestdeal":
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('command',), ('"bestdeal"',), chat_id)
            get_city.get_city(chat_id)

        elif call.data in ['London', 'New York', 'Paris']:
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('city',), (call.data.join(['''"''', '''"''']),), chat_id)
            user_data = get_user_data.get_user_data(chat_id)
            if user_data[2] == 'bestdeal':
                get_range_price.get_range_price(chat_id)
            else:
                get_amount.get_amount(chat_id)

        elif re.search(r'\d{,3}, \d{,3}', call.data):
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('range_price',), (call.data.join(['''"''', '''"''']),), chat_id)
            get_range_distance.get_range_distance(chat_id)

        elif call.data.startswith('dist_'):
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(
                ('range_distance',),
                (call.data.lstrip('dist_').join(['''"''', '''"''']),),
                chat_id
            )
            get_amount.get_amount(chat_id)

        elif call.data.startswith('amount_'):
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(
                ('amount',),
                (call.data.lstrip('amount_').join(['''"''', '''"''']),),
                chat_id
            )
            get_date.get_date(call.message)

        elif call.data.startswith('photo_'):
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(
                ('photo_amount',),
                (call.data.lstrip('photo_').join(['''"''', '''"''']),),
                chat_id
            )
            get_confirmation.get_confirmation(chat_id)

        elif call.data == "Yes":
            bot.answer_callback_query(call.id)
            user_data = get_user_data.get_user_data(chat_id)
            res = parsing.parsing(user_data)
            amount = len(res)
            if res == []:
                bot.send_message(chat_id, 'Я не смог ничего найти')
                delete_user_data.delete_user_data(chat_id)
                restart_key_board.restart(chat_id)
            else:
                if '$' in res[0][4]:
                    bot.send_message(chat_id, 'Я смог найти {} из {} отелей'.format(
                        amount,
                        user_data[6]
                    ))
                    for i in range(amount):
                        bot.send_message(
                            chat_id,
                            'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                            'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}, {photos}'.format(
                                name=res[i][0],
                                street=res[i][1],
                                distance=res[i][2],
                                price=res[i][3],
                                price_for_all=res[i][4],
                                photos=', '.join(res[i][5:])
                            ))
                    delete_user_data.delete_user_data(chat_id)
                    restart_key_board.restart(chat_id)
                else:
                    for i in range(amount):
                        bot.send_message(
                            chat_id,
                            'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                            'цена за ночь - {price}, {photos}'.format(
                                name=res[i][0],
                                street=res[i][1],
                                distance=res[i][2],
                                price=res[i][3],
                                photos=', '.join(res[i][4:])
                            ))
                    delete_user_data.delete_user_data(chat_id)
                    restart_key_board.restart(chat_id)

        elif call.data == "No":
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, 'Начнем сначала')
            delete_user_data.delete_user_data(chat_id)
            start_key_board.start_key_board(chat_id)

        elif call.data == 'yes_p':
            bot.answer_callback_query(call.id)
            get_photo_amount.get_photo_amount(chat_id)

        elif call.data == 'no_p':
            bot.answer_callback_query(call.id)
            update_user_info.update_user_info(('photo_amount',), ('"0"',), chat_id)
            get_confirmation.get_confirmation(chat_id)
