n=input().split(' ')
count=len(n)
while count>10 or count<3:
    print("Кількість сторін не може бути більше 10 і меньше 3")
    n=input().split(' ')
    count=len(n)
for i in range(0, len(n), 1):
    n[i]=int(n[i])
abc=('A','B','C','D','E','F','G','H','I','J')
masiv=[]
for i in range(0, count-1, 1):
    masiv.append(abc[i]+abc[i+1]+'='+str(n[i]))
masiv.append(abc[count-1]+abc[0]+'='+str(n[count-1]))
print(masiv)
n.sort()
print("Кількість", count)
print("Найбільша сторона",n[len(n)-1])