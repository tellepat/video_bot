from time import sleep
from random import randrange

import telebot
from os import listdir


def get_files(path: str = "video"):
    return listdir(path)


bot = telebot.TeleBot("API_KEY")
chat_id = 11111111

files = get_files()

session = []

while True:
    rand_index: int
    while True:
        rand_index = randrange(0, len(files))
        if not(rand_index in session):
            session.append(rand_index)
            if len(session) == len(files):
                session = []
            break
    video = open('video/' + files[rand_index], 'rb')
    bot.send_video(chat_id, video)
    sleep(3600 + randrange(1, 3600*8))
