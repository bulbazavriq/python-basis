a = input()

from data import data

print('Country: %s' % a)

for i in data:
    if i['country'] == a:     
        print('Capital: %s' % i['capital'])
        break
