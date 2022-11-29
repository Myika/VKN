import pylab
import numpy as np
def text_clear(text):
    import string
    for p in string.punctuation + '\n':
        if p in text:
            text = text.replace(p, '')
    return text

def counter(list_element):
    count = {}
    for element in list_element:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1

    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(sorted_values)

keys=[]
num=[]

a = open('/Users/llirik/Desktop/Univer/Lab16/text.txt')
text=a.read()

text = text_clear(text.lower())

list_word = text.split()
b=counter(list_word)
print(type(b))

for key in b:
    num.append(b[key])
print(num)


for key in b.keys():
    keys.append(key)
print(keys)

pylab.bar(key, num)
pylab.show()