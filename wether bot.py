import telebot
import requests
import json

bot = telebot.TeleBot('7807877922:AAEvHPBUZIlKWrFDSuJR2CCoTBX1NSAjCjk')
API = 'ef0edd48014fd260a773940389f3aa9f'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        if temp > 25.0:
            photo_path = 'hot.png'
            caption = f'Сейчас погода в городе "{city}" {temp}°C 🥵'
        elif temp < 5.0:
            photo_path = 'cold.png'
            caption = f'Сейчас погода в городе "{city}" {temp}°C 🥶'
        else:
            photo_path = 'cool.png'
            caption = f'Сейчас погода в городе "{city}" {temp}°C 🧣'

        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=caption)
    else:
        bot.send_message(message.chat.id, '❗ОШИБКА❗\nГород указан не верно!\nУкажите навание правильно!')


bot.polling()