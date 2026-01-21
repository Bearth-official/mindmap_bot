# keep_alive.py
# 用於保持 Render 免費 Web Service 活躍

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<h1>🐻 Bearth Bot is awake!</h1>'

@app.route('/health')
def health():
    return 'OK', 200

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.daemon = True
    server.start()
