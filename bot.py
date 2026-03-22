import telebot

TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "እንኳን ወደ KENO ROYAL በሰላም መጡ! ዌብሳይቱን ተጠቅመው ይጫወቱ።")

if __name__ == '__main__':
    bot.remove_webhook() # የቆየውን ግኑኝነት ያጸዳል
    print("ቦቱ በአዲሱ ቶከን ስራ ጀምሯል...")
    bot.polling(none_stop=True)
    
