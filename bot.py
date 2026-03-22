import telebot
import os

# የአዲሱ ቶከንህ ቦታ
TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "እንኳን ወደ KENO ROYAL በሰላም መጡ!")

if __name__ == '__main__':
    bot.remove_webhook()
    # Render ላይ እንዲሰራ ይሄን ይጠቀማል
    bot.polling(none_stop=True)
    
