import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7777564158:AAGN1oKNrtapo5XPRtQjDAqngoLwZCBnhBc')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет введите сумму')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
     amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат ввода! Вводите значение праильно!')

    if amount > 0.00:
        markup = types.InlineKeyboardMarkup(row_width=2)
        bt1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        bt2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        bt3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        bt5 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(bt1, bt2, bt3, bt5)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вводите значения больше 0!')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.split('/')
        res = currency.convert(amount, values[0].upper(), values[1].upper())  # Приводим к верхнему регистру
        bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}. Можете вписать сумму еще раз')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите значение через /')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0].upper(), values[1].upper())  # Приводим к верхнему регистру
        bot.send_message(message.chat.id, f'Получается {round(res, 2)}. Можете вписать сумму еще раз')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, f'Неправильный ввод. Введите значение заного')
        bot.register_next_step_handler(message.chat.id, my_currency)

bot.polling()