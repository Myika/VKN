import math 
x=float(input("Введіть х  "))
y=math.pow(4, 2*x) -math.log1p(math.cos(x))/2-(math.pow(x, 2)+1)**(1. / 3.)
print (y)