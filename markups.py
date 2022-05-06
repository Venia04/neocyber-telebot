import telebot


class Keyboard:
	def __init__(self, bot):
		self.bot = bot

	def main_menu(self, message):
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		user_markup.row('Записаться')
		hello_message = f'*Привет, {message.from_user.first_name}!*\
			\nЭто бот для записи в компьютерном клубе NeoCyber!\nДля записи просто\
			нажми кнопку *Записаться* внизу⬇\nА для отмены уже существующей записи позвони\
			админу клуба по номеру +375-29-123-45-67'
		self.bot.send_message(message.from_user.id, hello_message, reply_markup=user_markup, parse_mode='Markdown')

	def make_appointment(self, message):
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		user_markup.row('Компьютер')
		user_markup.row('Playstation')
		user_markup.row('VIP Компьютер')
		self.bot.send_message(message.from_user.id, 'Выберите Пакет:')
