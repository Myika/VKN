import json
from tkinter import *
import pylab
import numpy as np
keys=[]
text = open('/Users/llirik/Desktop/Univer/Lab 15/input.json')
a=text.read()


data=json.loads(a)
for item in data['finans']['month']:
    a=(item['january'],item['february'],item['march'], item['april'], item['may'], item['june'], item['july'], item['august'])
    for key in item.keys():
        keys.append(key)
        

pylab.bar(keys, a)
pylab.show()