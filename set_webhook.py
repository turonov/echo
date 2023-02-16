from telegram import Bot
import os

url = "https://turonov.pythonanywhere.com/webhook"

TOKEN = os.environ['TOKEN']
bot: Bot = Bot(TOKEN)


print(bot.set_webhook(url))