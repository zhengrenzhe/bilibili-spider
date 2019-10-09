import telegram

BOT_TOKEN = "957056376:AAEhnWPlIcUUcO5ze6hcbDlPQupjMAfXgCM"

bot = telegram.Bot(token=BOT_TOKEN)

print(bot.get_me())
