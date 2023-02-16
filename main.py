from telegram import Update
from telegram.ext import CallbackContext

def start(update:Update,context:CallbackContext):
    update.message.reply_text('welcom to our bot')

def echo(update:Update,context:CallbackContext):
    text = update.message.text
    update.message.reply_text(text)