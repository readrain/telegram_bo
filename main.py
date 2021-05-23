import telebot
from telebot import types

TOKEN = '1793555259:AAEr3r-ZnMntKuYvQNmiQ3ehR4ccPSf7tgc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Привет', 'Пока')
    markup.row("/start", '/hi')
    bot.send_message(message.chat.id, 'Привет человек', reply_markup=markup)


@bot.message_handler(commands=['inline'])
def inline(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Привет бот', callback_data='hi')
    item2 = types.InlineKeyboardButton('Пока', callback_data='hi1')
    markup.add(item, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def data(call):
    if call.message:
        if call.data == 'Привет ':
            bot.send_message(call.message.chat.id, 'Привет друг')
        elif call.data == 'Пока ':
            bot.send_message(call.message.chat.id, 'Пока друг')

@bot.message_handler(commands=[ "hi"])
def handler_new_member(message):
   bot.send_message(message.chat.id, "[{} {}](tg://user?id={}), 🤝 привет"
                     .format(message.from_user.first_name,
                             message.from_user.last_name, message.from_user.id), disable_web_page_preview=True, parse_mode="Markdown")



bot.polling()