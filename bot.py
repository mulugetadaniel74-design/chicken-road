import telebot
from telebot import types
import os

# የቦትህ ቶከን
TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🚀 ጨዋታውን ጀምር (Launch)')
    itembtn2 = types.KeyboardButton('💰 አከፋፈል')
    markup.add(itembtn1, itembtn2)
    
    bot.send_message(message.chat.id, "እንኳን ወደ KENO ROYAL በሰላም መጡ! ለመጫወት 'Launch' የሚለውን ይጫኑ።", reply_markup=markup)

# ወደ ጨዋታው ቀጥታ የሚወስድ ክፍል
@bot.message_handler(func=lambda message: message.text == '🚀 ጨዋታውን ጀምር (Launch)' or message.text == 'Launch')
def launch_game(message):
    markup = types.InlineKeyboardMarkup()
    # ሊንኩ ወደ ዋናው ገጽ (index.html) እንዲሄድ ተደርጓል
    play_button = types.InlineKeyboardButton(text="አሁኑኑ ተጫወት 🎮", url="https://daniel-zt06.onrender.com")
    markup.add(play_button)
    
    bot.send_message(message.chat.id, "የኬኖ ጨዋታ ዝግጁ ነው! ለመጀመር ከታች ያለውን ሊንክ ይጫኑ፦", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '💰 አከፋፈል')
def payment(message):
    payment_text = "💵 በቴሌብር (09XXXXXXXX) ከፈሉ በኋላ ደረሰኙን እዚህ ይላኩ።"
    bot.send_message(message.chat.id, payment_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
