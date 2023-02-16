from flask import Flask, request
import requests
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters

from main import(
    start,
    echo
)

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST'.'GET'])
def webhook():
    # get data from request
    if request.method =='GET':
        return 'hi from python '
    elif request.method == 'POST':
        data = request.get_json(force=True)

        dispatcher:Dispatcher = Dispatcher(bot, None, workers=0)
        update: Update = Update,de_json(data,bot)

        dispatcher.add_handler(CommandHandler('start', callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text, echo))

        dispatcher.process_update(update)

        return 'hello'

    # get chat_id, text from update
    chat_id = update.message.chat.id
    text = update.message.text

    # sendMessage
    bot.send_message(chat_id, text)

    return 'ok'
