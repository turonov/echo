from flask import Flask, request
import requests
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher

from main import(
    start,
    echo
)

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    data = request.get_json(force=True)

    dispatcher:Dispatcher = Dispatcher(bot, None, workerls=0)

    # update
    update: Update = Update.de_json(data, bot)

    dispatcher.add_handler(CommandHandler('start', callback=start))
    dispatcher.add_handler(MessageHandler(Fiters.text, echo))

    dispatcher.process_update(update)

    # get chat_id, text from update
    chat_id = update.message.chat.id
    text = update.message.text

    # sendMessage
    bot.send_message(chat_id, text)

    return 'ok'
