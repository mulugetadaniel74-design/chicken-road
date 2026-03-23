import telebot
import os
from flask import Flask
from threading import Thread
import time

# ያንተ አዲሱ ቦት ቶከን
TOKEN = "8398999747:AAGS7-Hc9sjBzBs7vu_Mjj8uiONpwfhxLgw"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Keno Royal Bot is Live!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "እንኳን ወደ KENO ROYAL በሰላም መጡ! 👋\n\nገንዘብ ለማውጣት ያሸነፉበትን ስክሪንሹት (Screenshot) እና የቴሌብር ስልክ ቁጥርዎን እዚህ ይላኩ።")

@bot.message_handler(content_types=['photo', 'text'])
def handle_messages(message):
    # መልእክት ሲላክ አንተ ጋር እንዲደርስ
    bot.reply_to(message, "መልእክትዎ ደርሶናል። በቅርቡ አረጋግጠን እንከፍላለን!")

def run_bot():
    try:
        bot.remove_webhook()
        time.sleep(1)
        print("Bot is starting...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # ቦቱን በሌላ Thread ያስነሳል
    Thread(target=run_bot).start()
    # ዌብሳይቱን Render በሚሰጠው Port ያስነሳል
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  
