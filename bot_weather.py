import requests
import datetime
import telebot
from telebot import types


token_owm = "119ac87c52216b635e08999f82f43a74"
tel_token = "1714588322:AAFG9-iecgQjlPSOmH9rnE-a7RD0nh6Paho"
bot = telebot.TeleBot(tel_token)


def weather(city, token):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = r.json()
        city = data["name"]
        temp_now = str(data["main"]["temp"]) + "C°"
        humidity = str(data["main"]["humidity"]) + "%"
        v_wind = str(data["wind"]["speed"]) + " m/c"
        sunrise = str(datetime.utcfromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")) + " UTC"
        sunset = str(datetime.utcfromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")) + " UTC"
        return city, temp_now, humidity, v_wind, sunrise, sunset
    except Exception as ex:
        return 0


@bot.message_handler(content_types=["text"])
def answering(msg):
    human_city = msg.text
    keys = types.InlineKeyboardMarkup()
    temp = types.InlineKeyboardButton(text="Температура", callback_data="температура")
    humidity = types.InlineKeyboardButton(text='Влажность', callback_data="влажность")
    wind = types.InlineKeyboardButton(text='Скорость ветра', callback_data="ветер")
    sun = types.InlineKeyboardButton(text='Восход/Закат', callback_data="солнце")
    keys.add(temp, humidity, wind, sun)
    bot.send_message(msg.from_user.id, text="Выбери, что хочешь узнать", reply_markup=keys)
    if msg.text == "/help":
        bot.send_message(msg.from_user.id, "Просто введи город")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    fu = call.data
    args = weather(human_city, token_owm)
    if args:
        if fu == "температура":
            message = f"Температура воздуха {args[1]}"
            bot.send_message(call.message.chat.id, message)
        if fu == "влажность":
            message = f"Влажность воздуха {args[2]}"
            bot.send_message(call.message.chat.id, message)
        if fu == "ветер":
            message = f"Скорость ветра {args[3]}"
            bot.send_message(call.message.chat.id, message)
        if fu == "солнце":
            message = f"Восход сегодня в {args[4]}\nЗакат сегодня в {args[5]}"
            bot.send_message(call.message.chat.id, message)
    else:
        bot.send_message(call.message.chat.id, "Убедитесь в том, что город существует и затем повторите попытку")

bot.polling(none_stop=True, interval=0)




