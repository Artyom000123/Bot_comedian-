
import telebot#Для работы с API Telegram
import random#Рандомайзер
from jokes_db import jok_db#Импортируем базу данных в которую будут записываться все прочитанные анегдоты
from pars_joke import pa_rs, jok_list#Импортируем анегтоты

pa_rs()#Парсим сайт

bot = telebot.TeleBot('1722275766:AAhhkhknmnbvfctGnmhf-zhPloB-mSYi5caktJsEs')# Token бота

#Кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('как дела','расскажи анекдот1', 'ещё')

#Реакция на команду start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)#После команды start выводятся кнопки

@bot.message_handler(content_types=['text'])#Говорим что будем работать с текстом
def diolog(message):
    if message.text.lower() == 'как дела':#Если мы пишем это, то
        a = ["Норм", "Хорошо", "Бывало и хуже", "10/10", "Терпим", "Как у лани, внутри удава"]#Перечень возможных ответов
        e = random.choice(a)#Выбираем случайный ответ из перечьня a и записываем в "e"
        bot.send_message(message.chat.id, e)#Выводим "e"
        bot.send_message(message.chat.id, 'Сам как?')
        
    elif message.text.lower() == 'расскажи анекдот1':#Если мы пишем это то или нажимаем на кнопку
        s = random.choice(jok_list)#Выбираем случайный ответ из списка jok_list и записываем в "s"
        bot.send_message(message.chat.id, 'Слушай')
        bot.send_message(message.chat.id, s)#Выводим "s"
        jok_db(s)
    
    elif message.text.lower() == 'ещё':
        bot.send_message(message.chat.id, 'Готово')
        jok_list.clear()#Очещяем список
        pa_rs()

    else:
        bot.send_message(message.chat.id, message.text)#Бот повторяет всё что мы пишем
        bot.send_message(message.chat.id, 'Я и дальше буду за тобой повтоять, извини')    	
        
bot.polling(none_stop = True)#Типо вечный цикл. True нужно чтобы каждый раз не писать /start
