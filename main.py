import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

make_appointment = 'Записаться'
button2 = 'Button 2'


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,f"*Привет, {message.from_user.first_name}!*\
	\nЭто бот для записи в компьютерном клубе NeoCyber!\nДля записи просто\
	нажми кнопку *Записаться* внизу⬇\nА для отмены уже существующей записи позвони\
	админу клуба по номеру +375-29-123-45-67", parse_mode="Markdown")
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	item1=types.KeyboardButton(make_appointment)
	markup.add(item1)
	bot.send_message(message.chat.id, 'Выберите вариант', reply_markup=markup)


@bot.message_handler(commands=['button'])
def button_message(message):
	pass


@bot.message_handler(content_types=['text'])
def message_reply(message):
	if message.text == make_appointment:
		bot.send_message(message.chat.id, "")


bot.polling(none_stop=True)