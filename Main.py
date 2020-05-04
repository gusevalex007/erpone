import requests
import telebot
from telebot import types

response = requests.get('http://185.75.181.51/InfoErp/hs/GetTickets/', auth = requests.auth.HTTPBasicAuth('usus', '123'))

total= response.text

bot = telebot.TeleBot('1271443472:AAEWba4JvbFKXVfJ5VOxuoZY2OiDrZF_4SM')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Сколько тикетов за год?')
    btn2 = types.KeyboardButton('Халюков')
    btn3 = types.KeyboardButton('Данильченко')
    btn4 = types.KeyboardButton('Аскапов')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные по решенным тикетам напишите " \
                   f"фамилию сотрудника, например: Данильченко и так далее\n\nЗаходи к нам на сайт <a href='https://new.erpone.ru'>ERP ONE</a>"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "данильченко":
        info = 1555
    elif get_message_bot == "халюков":
        info = 2311
    elif get_message_bot == "аскапов":
        info = 233
    else:
        info = total
    final_message = f"<u>Данные по тикетам:</u>\n<b>Решено: </b>{info:,}"
    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)