import telebot
from telebot import types
import os
import random
from PIL import ImageGrab
print(" * Bot is Online *\n")
print("#--------------#")
#---------------#
TOKEN = "1250722307:AAFEGLBcdLHd6h1IHi37ttS0Tzddffq2SEk"
bot = telebot.TeleBot(TOKEN)
#--------------#

def getfile(filename):
    myfile = open(filename, "r+")
    return myfile.read()
    myfile.close()


#---------------#

def tscreenshot(user):
	usertext = user.text
	userchatid = user.chat.id
	username = user.chat.username
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name

	bot.send_message(userchatid , "Taking Screen Shot.\n\nUploading...")
	shot =ImageGrab.grab()
	shot.save("ScreenShot.png")
	photo = open("ScrenShot.png","rb")
	bot.send_photo(userchatid , photo , caption="ScreenShot Taked.")
	photo.close()
	#--------------#

def powersubmenu(user):
	usertext = user.text
	userchatid = user.chat.id
	username = user.chat.username
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name
	#------

	dokmeha = types.ReplyKeyboardMarkup(row_width = 2 , resize_keyboard=True)
	dokme1 = types.KeyboardButton("🖥 ShutDown 🖥")
	dokme2 = types.KeyboardButton("♻️ Restart ♻️")
	dokme3 = types.KeyboardButton("🔙 Back 🔙")
	dokmeha.add(dokme1 , dokme2 , dokme3)
	bot.send_message(userchatid , "Power Sub Menu:" , reply_markup = dokmeha)

#---------------#

def putfile(filename, filedata):
    myfile = open(filename, "w+")
    return myfile.write(filedata)
    myfile.close()

#--------------#

def savetodb(user):
	usertext = user.text
	userchatid = user.chat.id
	username = user.chat.username
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name

	textnote = usertext.replace("/save ","")
	randn = random.randint(11111,99999)
	putfile("database/data-" + str(randn) + ".txt" , str(textnote))

	bot.send_message(userchatid , "Payam Shoma Ba ID " + str(randn) + " Save Shod.")

#--------------#

def dblist(user):
	usertext = user.text
	userchatid = user.chat.id
	userusername = user.chat.username
	userfirstname = user.chat.first_name
	userlastname = user.chat.last_name

	listfiles = ""
	for r, d, f in os.walk("database"):
		for file in f:
			listfiles = listfiles + "\n" + str(file)
		bot.send_message(userchatid , "Your Sava List :\n" + str(listfiles))

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
	Dokme1 = types.KeyboardButton("📸 ScreenShot 📸")
	Dokme2 = types.KeyboardButton("PowerOption")
	Dokme3 = types.KeyboardButton("🎧 PlaySound 🎧")
	Dokme4 = types.KeyboardButton("📂 FillManager 📂")
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
		if(usertext == "/start" or usertext == "🔙 Back 🔙"):
			
			bot.send_message(userchatid , "\n-----------------------Main-Menu-----------------------\n\nAdmin \"" + str(userfirstname) +"\"\n\n-Chat Off-\n\nEstefade az Robat Fagat ba Dokmeha." , reply_markup=Dokmeha)
		if (usertext == "/save"):
			bot.send_message(userchatid , "Bad az /save Fasele Bezarid va Matn Khod ra Type Konid.\n\n/save [message]")
		if(usertext.startswith("/save ")):
			savetodb(user)
		if (usertext == "/savelist"):
			dblist(user)
		if(usertext == "PowerOption"):
			powersubmenu(user)
		if(usertext == "📸 ScreenShot 📸"):
			tscreenshot(user)
	else:
		bot.send_message(userchatid , "\"" +userfirstname +"\"" + " Aziz: \n Shoma Ejaze Estefade az Robat \"Alireza'sOSremoter\" ra Nadarid.\n\nBaray Estefade be ID @UrmiaCoder Moraje Farmaeid.\n\n-Chat Off-" , reply_markup=Dokmeha)		

#---------------#
bot.polling(True)
