# import logging
import sqlite3
import config
import telebot
from markups import Keyboard
from telebot import types

#
# from uuid import uuid4
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
ADMIN = config.ADMIN
# путь к БД: рядом с папкой проекта папка neoDB
DB_PATH = '../neoDB/appoint.db'
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()
bot = telebot.TeleBot(config.TOKEN)
keyboard = Keyboard(bot)


# функция добавления информации в базу данных
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


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
    db_table_val(user_id=uid, user_name=uname, user_surname=usname, username=username)
    print(f"{uname}: {uid}")
    print('SUCCESS start command')


@bot.message_handler(func=lambda mess: "Главное меню" == mess.text, content_types=['text'])
def handle_text(message):
    keyboard.main_menu(message)


@bot.message_handler(func=lambda mess: "Записаться" == mess.text, content_types=['text'])
def handle_text(message):
    keyboard.make_appointment(message)


def run():
    bot.polling(non_stop=True)


run()
