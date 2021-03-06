import config
import telebot
from telebot import types
import sqlite3
import time
import threading


conn = sqlite3.connect('DB FOR BOT.db', check_same_thread=False)
cursor = conn.cursor()

global null
null="0"
global action2
action2="0"
global a
a="0"
global b
b="0"
global c
c="0"
global d
d="0"
global e
e="0"
global f
f="0"
global g
g="0"
global r
r="0"
global v
v="0"
global z
z="0"
global b1
b1="0"
global c1
c1="0"
global d1
d1="0"
global action
action="0"
global place
place="0"
global road
road="0"
global u
u="0"

bot=telebot.TeleBot(config.token)

def message_send():
    statTime = time.strftime("%H:%M")
    dateTime = time.strftime("%A")
    while True:
        if statTime == "19:59":
            make = types.ReplyKeyboardMarkup()
            buttion_1 = types.KeyboardButton(text="Я на объекте")
            buttion_2 = types.KeyboardButton(text="Я на работе")
            buttion_3 = types.KeyboardButton(text="Я дома")
            buttion_4 = types.KeyboardButton(text="Я в лаборотории")
            buttion_5 = types.KeyboardButton(text="Другое")
            make.add(buttion_1, buttion_2,buttion_3,buttion_4,buttion_5)
            bot.send_message(message.chat.id,"Где вы или чем заняты?",reply_markup=make)
        if dateTime==("Monday"):
            cursor.execute("SELECT DateTime, Action, PlaceProject, Action2, Road FROM Table_2 ORDER BY ID LIMIT ?",
                           (str(message.from_user.id)))
            result = cursor.fetchall()
            bot.send_message(message.chat.id, result)

#Реакция на комманду /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.send_message(message.chat.id,"Здравствуйте! Я бот для отчетов, каждый день нещадно с 9 утра спамить вас запросами об отчетах покуда вы не ответите. Вы сами на это подписались! Надеюсь наша работа с вами будет успешной.")

# Развитие событий "на объекте"
@bot.message_handler(regexp="Я на объекте")
def handle_message(message):
    workup = types.ReplyKeyboardMarkup()
    button_New = types.KeyboardButton(text="Объект новый")
    buttion_old = types.KeyboardButton(text="Объект старый")
    workup.add(button_New, buttion_old)
    bot.send_message(message.chat.id, "На каком объекте?", reply_markup=workup)
    global action
    action = message.text


@bot.message_handler(regexp="Объект новый")
def handle_message_id(message):
    bot.send_message(message.chat.id,
                     "Напишите название объекта. Помните вы не можете иметь более 3-х объектов")
    global a
    a = "1"


@bot.message_handler(regexp="Объект старый")
def handle_message_id(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if b != "0":
        buttion_one = types.KeyboardButton(b)
        maxup.add(buttion_one)
    if c != "0":
        buttion_two = types.KeyboardButton(c)
        maxup.add(buttion_two)
    if d != "0":
        buttion_three = types.KeyboardButton(d)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Напишите название объекта на котором вы сейчас", reply_markup=maxup)
    global a
    a = "1"


# Развитие событий "В лаборотории"
@bot.message_handler(regexp="Я в лаборотории")
def mess(message):
    work = types.ReplyKeyboardMarkup(row_width=1)
    buttion_new = types.KeyboardButton(text="Я занимаюсь чем-то новым")
    buttion_old = types.KeyboardButton(text="Я все еще работаю над одним из старых проектов")
    work.add(buttion_new, buttion_old)
    bot.send_message(message.chat.id, "Что вы там делаете?", reply_markup=work)
    global action
    action = message.text


@bot.message_handler(regexp="Я занимаюсь чем-то новым")
def new(message):
    bot.send_message(message.chat.id,
                     "Напишите название объекта. Помните вы не можете иметь более 3-х проектов")
    global z
    z = "1"


@bot.message_handler(regexp="Я все еще работаю над одним из старых проектов")
def handle_message_id(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if e != "0":
        buttion_one = types.KeyboardButton(e)
        maxup.add(buttion_one)
    if f != "0":
        buttion_two = types.KeyboardButton(f)
        maxup.add(buttion_two)
    if g != "0":
        buttion_three = types.KeyboardButton(g)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Напишите, чем именно вы сейчас заняты", reply_markup=maxup)
    global z
    z = "1"


# Реакция на "В дороге"
@bot.message_handler(regexp="Я в дороге")
def road_mess(message):
    bot.send_message(message.chat.id, "Куда вы едете?")
    global action
    action = message.text
    global r
    r = "1"


# Реакция на "Другое"
@bot.message_handler(regexp="Другое")
def other(message):
    bot.send_message(message.chat.id, "Напишите.")
    global action
    action = message.text
    global v
    v = "1"


# Реакция на "Дома"
@bot.message_handler(regexp="Я дома")
def other(message):
    bot.send_message(message.chat.id, "Ок")
    global action
    action = message.text
    global place
    place = "0"
    cursor.execute("INSERT INTO Table_2 VALUES(?,?,?,?,?,?)",
                   (time.asctime(), action, place, null, null, message.from_user.id))
    conn.commit()
    conn.close()

#Реакция на любой текст
@bot.message_handler(content_types=["text"])
def mesage_reaction(message):
    global r
    global a
    global b
    global c
    global d
    global place
    global b1
    global c1
    global d1
    global action2
    global road
    global z
    if road == "1":
        road = message.text
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(?,?,?,?,?,?)",
                       (time.asctime(), action, place, null, road, message.from_user.id))
        conn.commit()
        conn.close()
    if r == "0":
        pass
    elif r == "1":
        place = message.text
        bot.send_message(message.chat.id, "Зачем?")
        r = "0"
        road = "1"
    if v == "1":
        action2 = message.text
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(?,?,?,?,?,?)",
                       (time.asctime(), action, null, action2, null, message.from_user.id))
        conn.commit()
        conn.close()
    if z == "1":
        place = message.text
        z = "0"
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(?,?,?,?,?,?)",
                       (time.asctime(), action, place, null, null, message.from_user.id))
        conn.commit()
        conn.close()
    if a == "0":
        if b != "0":
            madup = types.ReplyKeyboardMarkup(row_width=1)
            buttion_delete = types.KeyboardButton(text="Да. Удалить объект")
            buttion_stay = types.KeyboardButton(text="Нет. Оставить")
            madup.add(buttion_delete, buttion_stay)
            bot.send_message(message.chat.id, "Вы закончили работу на нем?", reply_markup=madup)
            b1 = "1"
        if c != "0":
            madup = types.ReplyKeyboardMarkup(row_width=1)
            buttion_delete = types.KeyboardButton(text="Да. Удалить объект")
            buttion_stay = types.KeyboardButton(text="Нет. Оставить")
            madup.add(buttion_delete, buttion_stay)
            bot.send_message(message.chat.id, "Вы закончили работу на нем?", reply_markup=madup)
            c1 = "1"
        if d != "0":
            madup = types.ReplyKeyboardMarkup(row_width=1)
            buttion_delete = types.KeyboardButton(text="Да. Удалить объект")
            buttion_stay = types.KeyboardButton(text="Нет. Оставить")
            madup.add(buttion_delete, buttion_stay)
            bot.send_message(message.chat.id, "Вы закончили работу на нем?", reply_markup=madup)
            d1 = "1"
        if action2 == "1":
            action2 = message.text
            bot.send_message(message.chat.id, "Я запомню это")
            cursor.execute("INSERT INTO Table_2 VALUES(?,?,?,?,?,?)",
                           (time.asctime(), action, place, action2, null, message.from_user.id))
            conn.commit()
            conn.close()
    if a == "1":
        if b == "0":
            b = message.text
            if b != "0":
                c = message.text
                if c != "0":
                    d = message.text
        place = message.text
        bot.send_message(message.chat.id, "Что вы там делаете?")
        a = "0"
        action2 = "1"


if __name__ == '__main__':
    t = threading.Thread(target=message_send)
    t.start()
    bot.polling(none_stop=True)
