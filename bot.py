import telebot
import os

# ያንተ አዲሱ መረጃ
TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
MY_ID = "7313437942"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    text = message.text.split()
    if len(text) > 1:
        data = text[1]
        bot.send_message(MY_ID, f"🚀 አዲስ የገንዘብ ጥያቄ ደርሷል!\n\nዝርዝር፦ {data}")
        bot.reply_to(message, "ጥያቄዎ ለዳንኤል ተልኳል!")
    else:
        bot.reply_to(message, "ሰላም ዳንኤል! ቦቱ በ Render ላይ በትክክል እየሰራ ነው።")

# ለ Render እንዲመች
if __name__ == "__main__":
    print("Setgame bot is running on Render...")
    bot.polling(none_stop=True)
