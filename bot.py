import telebot

bot  = telebot.TeleBot("6132888039:AAF56JEayMkV6FFHdcHV6ts_Q9s9rqd1yGI")

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, "salom men takrorlovchi botman")

@bot.message_handler(func=lambda message:True)
def end_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()