import telebot

TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
MY_ID = "7313437942"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    text = message.text
    if "Withdraw" in text:
        bot.send_message(MY_ID, f"⚠️ **የማውጫ ጥያቄ!**\n\nከ፦ @{message.from_user.username}\nመረጃ፦ {text}")
        bot.reply_to(message, "ጥያቄዎ ለዳንኤል ደርሷል! በቅርቡ ይላክላችኋል።")
    elif "Deposit" in text:
        bot.reply_to(message, "እባክዎ የከፈሉበትን Screenshot (ፎቶ) አሁን ይላኩ።")
    else:
        bot.reply_to(message, "እንኳን ወደ Keno Royal መጡ! በዌብሳይቱ ላይ ቁጥሮችን መርጠው ይጫወቱ።")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo_id = message.photo[-1].file_id
    bot.send_photo(MY_ID, photo_id, caption=f"💰 **አዲስ የዲፖዚት ፎቶ!**\nከ፦ @{message.from_user.username}\nID: {message.from_user.id}")
    bot.reply_to(message, "ፎቶው ለዳንኤል ደርሷል፤ እናመሰግናለን!")

bot.polling(none_stop=True)
