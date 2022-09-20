import math 
a=int(input("Перший діапозон (a) "))
b=int(input("Дрегий діапозон (b) "))
h=int(input("Крок (h) "))
for x in range(a,b+1,h): 
  y=math.log(abs(x+math.e **x),3)
  print("%x x=%.1f     y=%.3f"%(x,x,y))      