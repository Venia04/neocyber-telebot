# import logging
import sqlite3
import config
import telebot
from db import BotDB
from markups import Keyboard
from telebot import types

#
# from uuid import uuid4
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
ADMIN = config.ADMIN

bot = telebot.TeleBot(config.TOKEN)
keyboard = Keyboard(bot)
# путь к БД: рядом с папкой проекта папка neoDB
BotDB = BotDB('../neoDB/appoint.db')

@bot.message_handler(commands=['start'])
def start_message(message):
    uid = message.from_user.id
    # if uid == ADMIN:
    #     keyboard.admin_func(message)
    # else:
    #     keyboard.main_menu(message)
    keyboard.main_menu(message)
    uname = message.from_user.first_name
    usname = message.from_user.last_name
    username = message.from_user.username
    if not BotDB.user_exists(user_id=uid):
        BotDB.add_user(user_id=uid)
    print(f"{uname}: {uid}")
    print('SUCCESS start command')


@bot.message_handler(func=lambda mess: "Главное меню" == mess.text,
                     content_types=['text'])
def handle_text(message):
    keyboard.main_menu(message)


@bot.message_handler(func=lambda mess: "Записаться" == mess.text,
                     content_types=['text'])
def handle_text(message):
    keyboard.make_appointment(message)


def run():
    bot.polling(non_stop=True)


run()
