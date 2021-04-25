import telebot
from telebot import types
import time


TOKEN = "1781580366:AAHDErGZwrLr6aiNRQuJ3asjqo7TgEgt3BY"
day_w, month, day, time, year = time.asctime().split()
bot = telebot.TeleBot(TOKEN)
greetings = ["Hello", "hello", "Привет", "привет", "Здравствуйте", "здраствуйте", "тевирп", "хай", "Салам", "Хай", "/start"]


@bot.message_handler(content_types=["text"])
def answering(msg):
    if msg.text in greetings:
        bot.send_message(msg.from_user.id, "Привет! Яндекс.Лицей нам не заплатил за это")
        keys = types.InlineKeyboardMarkup()
        timing = types.InlineKeyboardButton(text='Время', callback_data="время")
        dating = types.InlineKeyboardButton(text='Дата', callback_data="дата")
        keys.add(timing, dating)
        bot.send_message(msg.from_user.id, text="Выбери, что хочешь узнать", reply_markup=keys)
    elif msg.text == "/help":
        bot.send_message(msg.from_user.id, "Поздоровойся, где твои манеры?")
    else:
        bot.send_message(msg.from_user.id, "Моя твоя не понимать. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "время":
        message = f"Сейчас {time}"
        bot.send_message(call.message.chat.id, message)
    if call.data == "дата":
        message = f"{day_w}, {day} {month} {year}"
        bot.send_message(call.message.chat.id, message)


bot.polling(none_stop=True, interval=0)
