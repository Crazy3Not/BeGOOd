import telebot
import requests
import random

# Задаем токен вашего бота
TOKEN = '7156229717:AAG5kZZRAiTjAZhLTZkVF7FdlyQdacXBhWM'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки фотографии котика
def send_cat_photo(message):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    cat_photo_url = data[0]['url']
    bot.send_photo(message.chat.id, cat_photo_url)

# Функция для отправки фотографии песика
def send_dog_photo(message):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    dog_photo_url = data['message']
    bot.send_photo(message.chat.id, dog_photo_url)

# Функция для отправки гиф-изображения со страшными лицами
def send_scary_faces_gif(message):
    url = "https://api.giphy.com/v1/gifs/random"
    api_key = "vjKv4bD8olWpvjku0FIPt8j7bHZCyvDM"
    tag = "scary faces"
    params = {
        "api_key": api_key,
        "tag": tag,
        "rating": "pg-13",
        "limit": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['meta']['status'] == 200:
        gif_url = data['data']['images']['original']['url']
        bot.send_animation(message.chat.id, gif_url)
    else:
        bot.reply_to(message, "Извините, не удалось найти подходящее GIF-изображение.")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может отправлять фотографии животных. Просто отправь мне сообщение с текстом 'котик', 'песик' или 'попугай'.")

# Обработчик сообщений с текстом "котик"
@bot.message_handler(func=lambda message: message.text.lower() == 'котик')
def send_cat(message):
    send_cat_photo(message)

# Обработчик сообщений с текстом "песик"
@bot.message_handler(func=lambda message: message.text.lower() == 'песик')
def send_dog(message):
    send_dog_photo(message)
    
# Обработчик сообщений с текстом "попугай"
@bot.message_handler(func=lambda message: message.text.lower() == 'попугай')
def send_scary_faces(message):
    send_scary_faces_gif(message)

# Запускаем бота
bot.polling()
