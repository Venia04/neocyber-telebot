import telebot
from telebot.util import quick_markup


class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, message):
        user_markup = quick_markup({
            'Twitter': {'url': 'twitter.com'}
        })
        hello_message = f'*Привет, {message.from_user.first_name}!*\
\nЭто бот для записи в компьютерном клубе NeoCyber!\nДля записи просто \
нажми кнопку *Записаться* внизу⬇\nА для отмены уже существующей записи позвони \
админу клуба по номеру +375-29-123-45-67'
        self.bot.send_message(message.from_user.id, hello_message,
                              reply_markup=user_markup, parse_mode='Markdown')

    def make_appointment(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row('Компьютер')
        user_markup.row('Playstation')
        user_markup.row('VIP Компьютер')
        self.bot.send_message(message.from_user.id, 'Выберите Пакет:',
                              reply_markup=user_markup)

    def admin_func(self, message):
        kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        types = telebot.types
        kb.add(types.InlineKeyboardButton(text="Это"))
        kb.add(types.InlineKeyboardButton(text="тестовая"))
        kb.add(types.InlineKeyboardButton(text="функция"))
        kb.add(types.InlineKeyboardButton(text="для проверки."))
        self.bot.send_message(message.from_user.id, 'Добро пожаловать в Админ-панель!',
                              reply_markup=kb)
