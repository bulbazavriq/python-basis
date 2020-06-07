a = input()

from data import data

for i in data:
    if i['continent'] == a:     
        print(i['country'])



#Azia = {'Бахрейн':'Ханой','Бангладеш':'Ереван','Афганистан':'Баку'}
#Evrope = {'Бельгия':'Москва','Великобритания':'Берлин','Германия':'Париж'}