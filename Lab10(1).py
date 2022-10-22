from collections import Counter
text = open('/Users/llirik/Desktop/Univer/example.txt')
line=text.read().split()
cnt=0
masiv=[]
number=[]
for i,s in enumerate(line):
    if s.isdigit():
        masiv.append(s)
        cnt+= len(s) # считаем цифры
text.close()
res = open('/Users/llirik/Desktop/Univer/result.txt', 'w')
if cnt == 0:
    print("числа не обнаружены",file=res)
else:
    print("Всього чисел",cnt,file=res)
    b=''.join(masiv)
    x = [int(a) for a in str(b)]
    print("Цифри",dict(Counter(x)),file=res)
res.close()