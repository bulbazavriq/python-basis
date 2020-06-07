a = input()

from data import data

#print('Country: %s' % a)

for i in data:
    if i['country'] == a:     
        print(i['capital'])
        print(i['square'])
        print(i['qty'])
        print(i['continent'])
        break