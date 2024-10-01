import telebot
from telebot import types

bot = telebot.TeleBot('7807877922:AAEvHPBUZIlKWrFDSuJR2CCoTBX1NSAjCjk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Перейти на сайт')
    bt2 = types.KeyboardButton('Удалить фото')
    bt3 = types.KeyboardButton('изменить текст')
    markup.row(bt1)
    markup.row(bt2, bt3)
    file = open('./Screenshot_18.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=message)
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website in open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delite')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton('Перейти на сайт', url='https://ru.wikipedia.org/wiki/Python')
    bt2 = types.InlineKeyboardButton('Удалить фото', callback_data='delite')
    bt3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
    markup.row(bt1)
    markup.row(bt2, bt3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:  True)
def callback_message(callback):
    if callback.data == 'delite':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling()