import json
text = open('/Users/llirik/Desktop/Univer/text.txt')
a=text.read().split( )
mas1=[]
mas2=[]
mas3=[]
for word in a:
    if len(word) ==1: 
        mas1.append(word)
for word in a:
    if len(word) ==2: 
        mas2.append(word)
for word in a:
    if len(word) ==3: 
        mas3.append(word)
x=len(mas1) , len(mas2) , len(mas3)
with open('res.json','w')as json_file:
    json.dump(x, json_file, indent=1)