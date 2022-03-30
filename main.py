import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

button1 = 'Button 1'
button2 = 'Button 2'

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,"Привет, я бот для записи в NeoCyber!")

@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	item1=types.KeyboardButton(button1)
	markup.add(item1)
	markup.add(item1)
	bot.send_message(message.chat.id,'Выберите вариант', reply_markup=markup)

@bot.message_handler(content_types=['text'])
# def firstFunc(message):
# 	bot.send_message(message.chat.id, message.text)
# 	print(str(message.from_user.username) + " Message ID:" + str(message.id))
def message_reply(message):
	if message.text == button1:
		bot.send_message(message.chat.id,"Ти лох)")


bot.polling(none_stop=True)
