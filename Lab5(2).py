import math 
a=float(input("Введіть число a1:  "))
b=float(input("Введіть число b2:  ")) 
c=float(input("Введіть число c3:  "))
N=float(input("Введіть число N:  "))
if a % N == 0 and b % N == 0 and c % N == 0:
    print("N є спільним кратним")
else:
    print("N не є спільним кратним")
  