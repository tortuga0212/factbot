import requests
import random
import telebot
from bs4 import BeautifulSoup as b
URL = 'https://europaplus.ru/news/samye-interesnye-fakty-obo-vsem-na-svete'
API_KEY = '6343355419:AAEMhYJu7GtsV7TheRavtwjHRgmMrl8czuw'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    facts = soup.find_all ('p', class_='typography typography_type_text typography_size_max typography_mark_light')
    return [text.text for text in facts]

list_of_facts = parser(URL)
random.shuffle(list_of_facts)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Чтобы узнать что-то интересненькое, введите любую цифру:')

@bot.message_handler(content_types=['text'])
def facts(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_facts[0])
        del list_of_facts[0]
    else:
        bot.send_message(message.chat.id, 'Введите цифру от 1 до 9:')

bot.polling()