import telebot
from telebot import types
from random import choice

TOKEN = "1734028547:AAEOs9eDL8TpQLUeJIqGIypTM_rIqTDDs7c"
bot = telebot.TeleBot(TOKEN)


first = ["Сегодня — лучший день для начинаний.",
         "Отличный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут ухудшить здоровье.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

greetings = ["Hello", "hello", "Привет", "привет", "Здравствуйте", "здраствуйте", "тевирп", "хай", "Салам", "Хай", "/start"]

@bot.message_handler(content_types=["text"])
def answering(msg):
    if msg.text in greetings:
        bot.send_message(msg.from_user.id, "Приветствую, сейчас вам расскажу я гороскоп")
        keyboard = types.InlineKeyboardMarkup()
        oven = types.InlineKeyboardButton(text='Овен', callback_data="гороскоп")
        telec = types.InlineKeyboardButton(text='Телец', callback_data="гороскоп")
        bliz = types.InlineKeyboardButton(text='Близнецы', callback_data="гороскоп")
        rak = types.InlineKeyboardButton(text='Рак', callback_data="гороскоп")
        lev = types.InlineKeyboardButton(text='Лев', callback_data="гороскоп")
        deva = types.InlineKeyboardButton(text='Дева', callback_data="гороскоп")
        ves = types.InlineKeyboardButton(text='Весы', callback_data="гороскоп")
        scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data="гороскоп")
        strelec = types.InlineKeyboardButton(text='Стрелец', callback_data="гороскоп")
        kozerog = types.InlineKeyboardButton(text='Козерог', callback_data="гороскоп")
        vodoley = types.InlineKeyboardButton(text='Водолей', callback_data="гороскоп")
        fish = types.InlineKeyboardButton(text='Рыбы', callback_data="гороскоп")
        keyboard.add(oven, telec, bliz, rak, lev, deva, ves, scorpion, strelec, kozerog, vodoley, fish)
        bot.send_message(msg.from_user.id, text="Выбери свой знак зодиака", reply_markup=keyboard)
    elif msg.text == "/help":
        bot.send_message(msg.from_user.id, "Поздоровойся, где твои манеры?")
    else:
        bot.send_message(msg.from_user.id, "Моя твоя не понимать. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "гороскоп":
        message = choice(first) + " " + choice(second) + " " + choice(second_add) + " " + choice(third)
        bot.send_message(call.message.chat.id, message)

bot.polling(none_stop=True, interval=0)


