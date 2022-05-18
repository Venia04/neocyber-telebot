from markups import Keyboard
import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
keyboard = Keyboard(bot)


@bot.message_handler(commands=['start'])
def start_message(message):
	user_markup = types.ReplyKeyboardMarkup(True, False)

	user_markup.row('Записаться')

	hello_message = f'*Привет, {message.from_user.first_name}!*\
	\nЭто бот для записи в компьютерном клубе NeoCyber!\nДля записи просто\
	нажми кнопку *Записаться* внизу⬇\nА для отмены уже существующей записи позвони\
	админу клуба по номеру +375-29-123-45-67'

	bot.reply_to(message, hello_message, reply_markup=user_markup, parse_mode='Markdown')


@bot.message_handler(func=lambda mess: "Главное меню" == mess.text, content_types=['text'])
def handle_text(message):
	keyboard.main_menu(message)


@bot.message_handler(func=lambda mess: "Записаться" == mess.text, content_types=['text'])
def handle_text(message):
	keyboard.make_appointment(message)


bot.polling(non_stop=True)
