import math
import random
from array import* 
a=int(input("Ведіть кількість чисел "))
masiv=array('i',[])
for i in range (a):
    b=random.randint(0,10)
    masiv.append(b)
    print("Вивод елементів масива",masiv[i])
x=1
y=0
for i in range (a):
    if masiv[i]%2 == 0:
        x=x*masiv[i]
        y=y+1
        print(masiv[i])
if y==0:
    print("Нема парних елементів")
else:
    print(x)
    print(y)
    print("Геометр",pow(x,1/y))