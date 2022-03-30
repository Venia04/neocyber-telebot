import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
bot.remove_webhook()

@bot.message_handler(content_types=['text'])
def firstFunc(message):
	bot.send_message(message.chat.id, message.text)
	print(str(message.from_user.username) + " Message ID:" + str(message.id))

bot.polling(none_stop=True)