import math
a=int(input("Перший діапозон (a) "))
b=int(input("Дрегий діапозон (b) "))
h=int(input("Крок (h) "))
while a<=b:
    y=math.log(abs(a+math.e **a),3)
    print("%x a=%.1f     y=%.3f"%(a,a,y))
    a=a+h
