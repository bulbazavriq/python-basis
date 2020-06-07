a = input()
o = 0
from data import data

for i in data:
    if i['continent'] == a:     
        o += 1
print(o)

