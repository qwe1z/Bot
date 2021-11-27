import telebot
from telebot import types

token = "2107375073:AAGMRmPjgP8kH7dyxVEv_9PdWpVAHQJhofs"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Это бот посвящен Формуле-1!', reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Нажми /help, чтобы узнать, что я умею')
@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, 'Я умею:\n'
                                      '/video - эта команда позволит тебе увидеть Highlights.\n'
                                      '/teams - эта команда позволит тебе увидеть лучшие команды Формулы-1.\n'
                                      '/store - эта команда направит тебя на магазин Формулы-1 '
                                      'Напиши слово "Ютуб канал" чтобы перейти на официальный канал на ютубе\n'
                                      'Напиши слово "билеты", чтобы купить билет на ближайшие соревнования по F1\n'
                                      'Напиши слово "водители",чтобы уведеть лучших гонщиков 2021 года ', reply_markup=keyboard)
@bot.message_handler(commands=['video'])
def start_message1(message):
    bot.send_message(message.chat.id, '[Higlights](https://www.formula1.com/en/video.html)', parse_mode='Markdown')
@bot.message_handler(commands=['teams'])
def start_message2(message):
    bot.send_message(message.chat.id, '[Teams](https://www.formula1.com/en/teams.html)', parse_mode='Markdown')
@bot.message_handler(commands=['store'])
def start_message2(message):
    bot.send_message(message.chat.id, '[store](https://f1store.formula1.com/en/?_s=bm-fi-f1-prtsite-topnav-230720-jm)', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "билеты":
        bot.send_message(message.chat.id, 'https://tickets.formula1.com/en')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "водители":
        bot.send_message(message.chat.id, 'https://www.formula1.com/en/drivers.html')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "Ютуб канал":
        bot.send_message(message.chat.id, 'https://www.youtube.com/c/F1')



bot.infinity_polling()