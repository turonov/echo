from telegram import Update
from telegram.ext import CallbackConxtext

def start(update:Update,context:CallbackConxtext):
    update.message.reply_text('welcom to our bot')

def echo(update:Update,context:CallbackConxtext):
    text = update.message.text
    update.message.reply_text(text)