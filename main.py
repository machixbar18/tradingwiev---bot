from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Configuraciones desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.json

    # Leer los campos del mensaje
    operacion = data.get("operacion", "Operacion no especificada")
    ticker = data.get("ticker", "Activo desconocido")
    entrada = data.get("entrada", "No definida")
    stop_loss = data.get("stop_loss", "No definido")
    take_profit = data.get("take_profit", "No definido")
    razon = data.get("razon", "Sin motivo especificado")
    timeframe = data.get("timeframe", "Temporalidad no definida")

    # Elegir ícono según tipo de operacion
    icono = "🚀" if operacion.lower() == "compra" else "🚨"

    # Construir el mensaje
    mensaje = f"{icono} Oportunidad de {operacion.upper()} en {ticker}\n\n"
    mensaje += f"Entrada: {entrada}\n"
    mensaje += f"Stop Loss: {stop_loss}\n"
    mensaje += f"Take Profit: {take_profit}\n"
    mensaje += f"Motivo: {razon}\n"
    mensaje += f"Marco temporal: {timeframe}"

    # Enviar mensaje a Telegram
    send_telegram_message(mensaje)
    return 'OK', 200

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
