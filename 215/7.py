a = input()
o = 0
from data import data

for i in data:
    if i['continent'] == a:     
        o += i['square']
print(o)
        
