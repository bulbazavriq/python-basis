# Получение названия страны по имени столицы
a = input()

from data import data



for i in data:
    if i['capital'] == a:     
        print(i['country'])
        break

