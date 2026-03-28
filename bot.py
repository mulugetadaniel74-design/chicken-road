import telebot
from telebot import types

TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)

# የክፍያ መረጃ (እዚህ ላይ ያንተን ስልክ ወይም አካውንት መቀየር ትችላለህ)
PAYMENT_INFO = """
💵 **የአከፋፈል መመሪያ**

1. በሲቢኢ ብር (CBE Birr) ወይም በቴሌብር (telebirr) መክፈል ይችላሉ።
2. የከፈሉበትን ደረሰኝ (Screenshot) እዚህ ይላኩ።
3. ክፍያዎ ሲረጋገጥ ጨዋታው ይጀምራል።

የመክፈያ ስልክ፡ 09XXXXXXXX (ዳንኤል)
"""

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🚀 ጨዋታውን ጀምር (Launch)')
    itembtn2 = types.KeyboardButton('💰 አከፋፈል')
    itembtn3 = types.KeyboardButton('📜 የጨዋታ ህግ')
    markup.add(itembtn1, itembtn2, itembtn3)
    
    bot.send_message(message.chat.id, "እንኳን ወደ ዳንኤል ኬኖ (Keno Royal) በሰላም መጡ! ምን መርዳት እችላለሁ?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🚀 ጨዋታውን ጀምር (Launch)' or message.text == 'Launch')
def launch_game(message):
    # እዚህ ጋር ወደ ዌብሳይትህ የሚወስድ ሊንክ መጨመር ትችላለህ
    markup = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton(text="አሁኑኑ ተጫወት 🎮", url="https://daniel-zt06.onrender.com")
    markup.add(play_button)
    
    bot.send_message(message.chat.id, "የኬኖ ጨዋታ ለመጀመር ዝግጁ ነዎት! ከታች ያለውን ሊንክ ተጭነው ይግቡ።", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '💰 አከፋፈል')
def payment(message):
    bot.send_message(message.chat.id, PAYMENT_INFO, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '📜 የጨዋታ ህግ')
def rules(message):
    rules_text = "ከ 1 እስከ 80 ባሉ ቁጥሮች ውስጥ የሚወዱትን ይምረጡ። 20 ቁጥሮች ይወጣሉ፤ የእርስዎ ቁጥሮች ከወጡ ያሸንፋሉ!"
    bot.send_message(message.chat.id, rules_text)

if __name__ == '__main__':
    print("ቦቱ በስኬት እየሰራ ነው...")
    bot.polling(none_stop=True)
    
