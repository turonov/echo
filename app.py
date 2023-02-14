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
    data = request.get_json(force=True)

    print(data)

    return 'ok'
