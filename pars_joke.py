import requests#Для потключения к сайту
from bs4 import BeautifulSoup#Для збора информации
jok_list = []#Создаём список в который всё и засунем
room = 2
def pa_rs():
	global room

	#Указываем сайт и страницу с которых всё и достанем
	HOST = 'https://nekdo.ru'#Сайт который парсим
	URL = f'https://nekdo.ru/page/{room}/'#Страница которую парсим

	

	#Это нужно чтобы нас не пощитали за ботов
	HEADERS = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'user-agent': '*/*'
	}

	#Достаём весь html со строницы?
	def get_html(url, params = ''):
		r = requests.get(url, headers = HEADERS, params = params)#Потключаемся к сайту
		return r


	def get_content(html):
		soup = BeautifulSoup(html, 'html.parser')#Говолим что делаем
		items = soup.find_all('div', class_='text')#Говорим откуда именно забираем html код

		for i in items:
		
			#append записывает то что находится в переменной i в конец списка jok_list
			jok_list.append(i.text)#Говорим в каком формате мы всё это записываем тоесть не просто html код тега div а текст который там находится

	def parse():
		html = get_html(URL)#Запускаем функцию get_html чтобы потключится к сайту
		if html.status_code == 200:#Если потключение прошло успешно
			get_content(html.text)#Вытаскиваем контент
			
		else:#При любых других обстоятельствах
			print("Жопа бро")
			
	parse()
	room+=1

