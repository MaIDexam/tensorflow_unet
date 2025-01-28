# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from detect import detect_human, import_weights_of_network
from telegram_bot import registrator, messege_sender, open_database, connect_bot
import telebot
import cv2
import threading
filename = 'users.json'
bot = connect_bot('6103459618:AAH4NBgtaD7GUOLYySMfPcGi8bfq3jcslZA')
users = open_database(filename)
model = import_weights_of_network('model.h5')
camera = cv2.VideoCapture(0)
def recording(bot, users, model, camera):
    while 1:
        b, date = detect_human(model, camera)
        if b:
            messege_sender(bot, users, 'images/'+date+'.jpg')
#registrator(bot, filename, users)
t1 = threading.Thread(target=registrator, args=(bot, filename, users,))
t2 = threading.Thread(target=recording, args=(bot, users, model, camera))
t1.start()
t2.start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#t.me/camera2398_bot - телеграм бот