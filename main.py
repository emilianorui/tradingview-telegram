from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Reemplaza con tus datos reales de Telegram
TELEGRAM_TOKEN = "894857295:AAGbfZMbS7CMkZrNtPRQvHq4-hHNeovAVBQ"
TELEGRAM_CHAT_ID = "1514103218"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    if data:
        send_telegram_message(f"🚨 *Alerta TradingView* 🚨\n\n{data}")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
