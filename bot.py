import telebot

TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
MY_ID = "7313437942" # የዳንኤል ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "ሰላም! የገንዘብ ጥያቄ ካለህ እባክህ የከፈልክበትን Screenshot (ፎቶ) ላክ።")

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    # ፎቶውን ለዳንኤል ያስተላልፋል
    photo_id = message.photo[-1].file_id
    caption = f"🚀 አዲስ የገንዘብ ማረጋገጫ ደርሷል!\n\nከ፦ @{message.from_user.username}\nID፦ {message.from_user.id}"
    
    bot.send_photo(MY_ID, photo_id, caption=caption)
    bot.reply_to(message, "ማረጋገጫው ለዳንኤል ተልኳል። በ 2 ደቂቃ ውስጥ ይጨመርልሃል! ✅")

if __name__ == "__main__":
    print("ቦቱ ፎቶ ለመቀበል ዝግጁ ነው...")
    bot.polling(none_stop=True)
