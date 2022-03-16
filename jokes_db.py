
import sqlite3

"""Курсор (sql) и блок кода с заполнением базы данными, должны быть в одной функции """
def jok_db (b):
    o = 1
    db = sqlite3.connect('jokes.db')#Создаём базу данных которая называется jokes и подключаемся к ней
    sql = db.cursor()#Создаём переменную sql хронящюю в себе cursor

    #Создаём таблицу anecdot если она не созданна (IF NOT EXISTS), со столбцами: number, joke
    sql.execute("""CREATE TABLE IF NOT EXISTS anecdot (
            number INT,
        joke  TEXT
            
    )""")
    db.commit()#Потверждаем наше действие

    #Щётчик для того чтобы номера в базе шли друг за другом
    while True:
        sql.execute(f"SELECT number FROM anecdot WHERE number = '{o}'")#Берём номер для проверки его уникальности

        if sql.fetchone() is None:#Если такого нрмена ещё нет то
            break#Останавливаем цикл и идём записывать

        else:#Иначе, тоесть если такой номер уже есть то
            o = o + 1#Меняем номер и проверяем ещё раз
    
    #Проверка уникальности анекдота
    sql.execute(f"SELECT joke FROM anecdot WHERE joke = '{b}'")#Беррём анекдот для проверки уникальности

    if sql.fetchone() is None:#Если такого анекдота ешё нет
        
        sql.execute(f"INSERT INTO anecdot VALUES (?, ?)", (o, b ))#Заливаем в таблицу информацию
        db.commit()#Потверждаем наше действие
        
    #Выводим таблицу
    for value1 in sql.execute("SELECT * FROM anecdot"):
        print(value1)
    print('')
    print('')
    print('')

