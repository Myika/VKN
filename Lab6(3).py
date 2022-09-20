from distutils.spawn import spawn
import math
a=int(input("Перший діапозон (a) "))
b=int(input("Дрегий діапозон (b) "))
h=int(input("Крок (h) "))
spisok=[]
while a<=b:
    y=math.log(abs(a+math.e **a),3)
    spisok.append(y)
    print(y,sep="/n")
    a=a+h
print("")
print("Середнє арифметичне", sum(spisok)/len(spisok))