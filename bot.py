import telebot
#---------------#
TOKEN = "1250722307:AAFEGLBcdLHd6h1IHi37ttS0Tzddffq2SEk"
bot = telebot.TeleBot(TOKEN)
#--------------#

@bot.message_handler(content_types=['text'])
def botmain(user):
	usertext = user.text
	userchatid = user.chat.id
	username = user.chat.id
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name
	if (userchatid == 1017719550):
		bot.send_message(userchatid,"Salam " + userfirstname)
	else:
		bot.send_message(userchatid , userfirstname + " Shoma Ejaze Estefade az Robat \"Alireza'sOSremoter\" ra Nadarid.")
	

#---------------#
bot.polling(True)
