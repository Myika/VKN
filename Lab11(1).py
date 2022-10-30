import random
quest = open('/Users/llirik/Desktop/Univer/quest.csv')
text=quest.read().split('\n')
print(text)
random.shuffle(text)
mas = []
for i in text:
  if i not in mas:
    mas.append(i)
print(mas)