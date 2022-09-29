import math
x=float(input("Перший діапозон (a) "))
b=float(input("Дрегий діапозон (b) "))
h=float(input("Крок (h) "))
while x<=b:
    y=math.log(abs(x+math.e **x),3)
    print("x=%.1f     y=%.3f"%(x,y))
    x=x+h
