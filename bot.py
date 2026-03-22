if __name__ == '__main__':
    # የቀድሞውን ግንኙነት በሙሉ ያጸዳል
    bot.remove_webhook()
    print("ቦቱ ስራ ጀምሯል...")
    # ስህተት ቢመጣ እንኳ ራሱ እንዲያስተካክል
    bot.polling(none_stop=True, interval=0, timeout=20)
