import math 
x=float(input("Введіть х  "))
def f1(x1):
     rez=math.log(abs(x1+1))
     return(rez)
def f2(x2):
     rez=math.sqrt(math.log1p(abs(math.cos(x2))))
     return(rez)
def f3(x3):
     rez=math.pow(x3, 2) + 4* abs(x3 - 4)+math.pow(math.e, x3)
     return(rez)
y=0.0
if x >= 7.2:
    y=f1(x)
elif -5.11 < x < 7.2:
    y=f2(x)
elif x <= -5.11:
    y=f3(x)
print(y)