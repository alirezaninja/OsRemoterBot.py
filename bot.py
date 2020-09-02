import telebot
from telebot import types
import os
print(" * Bot is Online *\n")
print("#--------------#")
#---------------#
TOKEN = "1250722307:AAFEGLBcdLHd6h1IHi37ttS0Tzddffq2SEk"
bot = telebot.TeleBot(TOKEN)
#--------------#

@bot.message_handler(content_types=['text'])

def botmain(user):
	usertext = user.text
	userchatid = user.chat.id
	username = user.chat.username
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name

	#--------------#

	Dokmeha = types.ReplyKeyboardMarkup(resize_keyboard=True)
	Dokme1 = types.KeyboardButton("ScreenShot")
	Dokme2 = types.KeyboardButton("PowerOptions")
	Dokme3 = types.KeyboardButton("PlaySound")
	Dokme4 = types.KeyboardButton("FillManager")
	Dokmeha.add(Dokme1 , Dokme2 , Dokme3 , Dokme4)

	#--------------#

	print("Command Send From:\nUserChatID => " + str(userchatid))

	if(username == None):
		pass
	else:
		print("UserName => @" + str(username))

	print("FirstName => " + str(userfirstname))
	print("UserTxt => " + str(usertext))
	print("\n#--------------# \n\n")

	#--------------#

	if (userchatid == 1017719550):
		if(usertext == "/start"):
			bot.send_message(userchatid , "Slm Admin \"" + str(userfirstname) +"\"\n\n-Chat Off-\n\nEstefade az Robat Fagat ba Dokmeha." , reply_markup=Dokmeha)		
	else:
		bot.send_message(userchatid , "\"" +userfirstname +"\"" + " Aziz: \n Shoma Ejaze Estefade az Robat \"Alireza'sOSremoter\" ra Nadarid.\n\nBaray Estefade be ID @UrmiaCoder Moraje Farmaeid.\n\n-Chat Off-" , reply_markup=Dokmeha)		

#---------------#
bot.polling(True)
