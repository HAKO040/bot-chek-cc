admin = 5706011922
token = input('TOKEN BOT:6830795432:AAGvQ2niBOdL7KqoLyZxecslaGTjqt2JTIc ')
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	id = message.from_user.id
	if not id == admin:
		bot.reply_to(message,'عذا هذا البوت خاص\n @H_D_il / @H_D_il')
	else:
			import os
        os.system("python AUTH-JOKER.py")
