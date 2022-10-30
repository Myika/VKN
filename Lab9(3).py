import operator
a=int(input("Довжина AB: "))
b=int(input("Довжина BC: "))
c=int(input("Довжина CD: "))
d=int(input("Довжина DE: "))
e=int(input("Довжина EF: "))
f=int(input("Довжина FG: "))
g=int(input("Довжина GA: "))
dict={"AB":0, "BC":0, "CD":0, "DE":0, "EF":0, "FG":0, "GA":0}
dict["AB"]=a
dict["BC"]=b
dict["CD"]=c
dict["DE"]=d
dict["EF"]=e
dict["FG"]=f
dict["GA"]=g
print(dict)
print("Кількість сторін:",len(dict))
print("Найбільший відрізок",max(dict.items(), key=operator.itemgetter(1)))
x=input("Видалити відрізок: ")
poppedItem = dict.pop(x)
print("Сума усіх сторін",sum(dict.values()))