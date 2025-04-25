
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = f"🚨 Alerta de TradingView:\n\n{data.get('message', 'Sin mensaje recibido')}"
    send_telegram_message(message)
    return 'OK', 200

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

app.run(host='0.0.0.0', port=10000)
