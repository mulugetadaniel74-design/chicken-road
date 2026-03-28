import telebot
import os

# የአዲሱ ቶከንህ ቦታ
TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)

# ለ /start ትዕዛዝ የሚሰጠው ምላሽ
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "እንኳን ወደ KENO ROYAL በሰላም መጡ! ለመጫወት ዝግጁ ነዎት?")

# በፎቶው ላይ ያየነው "Launch" የሚለውን ቃል ሲያይ የሚሰጠው ምላሽ
@bot.message_handler(func=lambda message: message.text == "Launch")
def launch_game(message):
    bot.reply_to(message, "የኬኖ ጨዋታ ለመጀመር ተዘጋጅተዋል! ዕድለኛ ቁጥሮችዎን ይምረጡ።")

# ሌሎች ቃላትን ሲጽፉ (ለምሳሌ ሰላምታ)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "እንኳን ወደ ዳንኤል ኬኖ ጨዋታ መጡ! ጨዋታውን ለመጀመር 'Launch' የሚለውን ይጫኑ ወይም /start ይበሉ::")

if __name__ == '__main__':
    print("ቦቱ መስራት ጀምሯል...")
    bot.remove_webhook()
    bot.polling(none_stop=True)
    
