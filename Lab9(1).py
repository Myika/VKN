import numpy
a=input("Введіть першу літеру ")
n=int(input("Кількість букв "))
abc=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
b=''
for i in range (26):
    if abc[i] == a:
        for j in range(i, i+n*4, 1):
            b=b+abc[j]
for i in range(0, len(b), n):
    print(b[i:i+n])