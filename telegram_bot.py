import telebot
import json
from time import sleep
def connect_bot(token):
    bot = telebot.TeleBot(token)
    return bot

def open_database(filename):
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

def rewrite_database(filename, users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def registrator(bot, filename, users):
    @bot.message_handler(commands=['start'])
    def message_send(message):
        if message.chat.id not in users:
            bot.send_message(message.chat.id, 'введите пароль')

    @bot.message_handler(content_types='text')
    def message_send(message):
        if message.chat.id not in users:
            if message.text == '1':
                users.append(message.chat.id)
                bot.send_message(message.chat.id, 'пароль верный')
                rewrite_database(filename, users)
                print(users)
            else:
                bot.send_message(message.chat.id, 'пароль неверный')

    bot.polling(none_stop=True)

def messege_sender(bot, users, file):
        sleep(1)
        for user in users:
            with open(file, 'rb') as file_rb:
                bot.send_document(user, file_rb)
