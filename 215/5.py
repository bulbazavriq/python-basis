a = input()

from data import data

for i in data:
    if i['country'] == a:     
        print(i['qty'] // i['square'])
        break
