# ኮዱ መጨረሻ ላይ ይሄ መኖሩን እይ
if __name__ == '__main__':
    bot.remove_webhook() # የቆየ ግኑኝነት ካለ እንዲያጸዳ
    print("ቦቱ ስራ ጀምሯል...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
    
