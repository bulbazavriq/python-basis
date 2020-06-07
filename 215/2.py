# Получение названия страны по имени столицы
a = 'Moscow'

from data import data

print('Country: %s' % a)

for i in data:
    if i['capital'] == a:     
        print('Capital: %s' % i['country'])
        break

