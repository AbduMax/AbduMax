from telebot import TeleBot
import json
import requests
from keyboards import *
from telebot.types import LabeledPrice

bot = TeleBot('1743514839:AAG-NqsB4Naa7O3RTH-FxTdxAI2TWSaMoRU')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    try:
        full_name = message.from_user.first_name + ' ' + message.from_user.last_name
    except TypeError:
        full_name = message.from_user.first_name
    bot.send_message(chat_id, f""" Assalomu alaykum  {full_name} \nЗдравствуйте  {full_name} """)
    choice_region(message)


def choice_region(message):
    chat_id = message.chat.id
    user_message = bot.send_message(chat_id, f'\n\n\nShaharni tanlang !   |    Выберите город!',
                                    reply_markup=generate_pagination())
    bot.register_next_step_handler(user_message, get_region)


def get_region(message):
    chat_id = message.chat.id
    params = {
        'q': message.text,
        'appid': '8eea3ada9503b752907f54e56dea0c44',
        # 'appid':'e39ce5d12420e3b12bcb9ff17f256b24',
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?', params)
        response_json = response.json()

        city_name = response_json['name']
        weather = response_json['weather'][0]['main']
        weather_desc = response_json['weather'][0]['description']
        wind_speed = response_json['wind']['speed']
        clouds = response_json['clouds']['all']
        temp = response_json['main']['temp']
        feels_like = response_json['main']['feels_like']
        humidity = response_json['main']['humidity']

        weather_message_ru = f"""Погода в городе {city_name}
            Сегодня - {weather}, {weather_desc}
            Облачность - {clouds} %
            Скорость ветра - {wind_speed} м/c
            Температура - {temp}
            Чувствуется как - {feels_like}
            Влажность - {humidity} %
                \n"""
        weather_message_uz = f"""{city_name} shaharida ob-havo 
            Bugun - {weather}, {weather_desc}
            Bulutlar (foizda) - {clouds} %
            Shamol tezligi - {wind_speed} м/c
            Harorat - {temp}
            Namlik - {humidity} %
                \n"""
        bot.send_message(chat_id, f'{weather_message_ru}     {weather_message_uz} ',)
        choice_region(message)

    except requests.HTTPError:
        print(f'Ошибка {response.status_code}')


bot.polling(none_stop=True)
