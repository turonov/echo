from flask import Flask, request
import requests
import os

# flask app
app = Flask(__name__)

# TOKEN
TOKEN = os.environ['TOKEN']


@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    update = request.get_json(force=True)

    # get chat_id, text from update
    chat_id = update['message']['from']['id']
    text = update['message']['text']

    # sendMessage
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=payload)

    return 'ok'
