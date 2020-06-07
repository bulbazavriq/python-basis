a = input()

from data import data

for i in data:
    if i['country'] == a:
        print(i['capital'])
        break

