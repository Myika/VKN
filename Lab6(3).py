import math
a=float(input("Перший діапозон (a) "))
b=float(input("Дрегий діапозон (b) "))
h=float(input("Крок (h) "))
spisok=[]
while a<=b:
    y=math.log(abs(a+math.e **a),3)
    spisok.append(y)
    print(y,sep="/n")
    a=a+h
print("")
print("Середнє арифметичне", sum(spisok)/len(spisok))