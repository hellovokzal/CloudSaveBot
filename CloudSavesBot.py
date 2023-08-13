import telebot
import os
bot = telebot.TeleBot("6321245464:AAHkVpANVic7UnixPLqxLcik-Rg7ciVZgJs")
@bot.message_handler(commands=['start'])
def start(message):
	print(f"{message.chat.id}: {message.text}")
	bot.send_message(message.chat.id, "Хранитель Текстов: Добро пожаловать в Хранитель Текстов! Вводите команды:\n/new <текст> - сохранить текст\n/view - посмотреть сохраненнве тексты\n/reg - зарегестрировать свой ID\n/delete - удалить ваш ID\n/users - посмотреть сколько челов зарегано")
@bot.message_handler(commands=['new'])
def new(message):
	print(f"{message.chat.id}: {message.text}")
	if os.path.isfile(f"{message.chat.id}.txt"):
		with open(f"{message.chat.id}.txt", "r") as file:
			myfile = file.read()
		with open(f"{message.chat.id}.txt", "w") as file:
			text = message.text[5:len(message.text)]
			file.write(f"{myfile}\n------------------------\n{text}")
			bot.send_message(message.chat.id, "Текст создан!")
	else:
		bot.send_message(message.chat.id, "Вы не зарегестрированы! Введите команду /reg, чтобы зарегестрировать ID")
@bot.message_handler(commands=['view'])
def view(message):
	print(f"{message.chat.id}: {message.text}")
	if os.path.isfile(f"{message.chat.id}.txt"):
		with open(f"{message.chat.id}.txt", "r") as file:
			send = file.read()
			bot.send_message(message.chat.id, send)
	else:
		bot.send_message(message.chat.id, "Вы не зарегестрированы! Введите команду /reg, чтобы зарегестрировать ID")
@bot.message_handler(commands=['reg'])
def reg(message):
	print(f"{message.chat.id}: {message.text}")
	if os.path.isfile(f"{message.chat.id}.txt"):
		bot.send_message(message.chat.id, "Вы зарегестрированы!")
	else:
		bot.send_message(message.chat.id, "Регестрируем ID...")
		with open(f"{message.chat.id}.txt", "w") as file:
			file.write("")
			bot.send_message(message.chat.id, "Успешно зарегестрирован ваш ID!")
@bot.message_handler(commands=['delete'])
def delete(message):
	print(f"{message.chat.id}: {message.text}")
	if os.path.isfile(f"{message.chat.id}.txt"):
		os.remove(f"{message.chat.id}.txt")
		bot.send_message(message.chat.id, "Успешно удалено!")
	else:
		bot.send_message(message.chat.id, "Вы уже удалены!")
bot.polling(none_stop=True)
@bot.message_handler(commands=['users'])
def users(message):
	bot.send_message(message.chat.id, f"Челов зарегано: `{num}")
