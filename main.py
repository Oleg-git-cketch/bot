import telebot
import webbrowser

bot = telebot.TeleBot('7807877922:AAEvHPBUZIlKWrFDSuJR2CCoTBX1NSAjCjk')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ru.wikipedia.org/wiki/Python')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.last_name}' )

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')

bot.polling()