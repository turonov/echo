import requests
import os

url = "http://turonov.pythonanywhere.com/webhook"

TOKEN = os.environ['TOKEN']
payload = {
    'url': url
}


r = requests.get(f'https://api.telegram.org/bot<TOKEN>/ser_webhook', params=payload)
print(r.status_code)