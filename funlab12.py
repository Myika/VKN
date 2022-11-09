import random
def nomer10(n):
    n1=int(n)
    st='ABCDEFGHIKLMNOPQRSTVXYZ'
    s=''
    for i in range(n1):
        x=random.choice(st)
        s=s+x
    return(s)

def nomer12(n):
    n1=int(n)
    st='ABCDEFGHIKLMNOPQRSTVXYZ'
    s=''
    for i in range(n1):
        x=random.choice(st)
        s=s+x
    return(s)

def bukv(s):
    golosni='АЕЄИІЇОУЮЯаеєиіїоуюя'
    a=0
    for i in range(len(s)):
        if s[i] in golosni:
            a +=1
    print("Кількість голосних",a)

def powpl(p,R,h):
    S=2*p*R*(R+h)
    print("Повна площа поверхні прямого циліндра",S)

def bichpl(p,R,h):
    S=2*p*R*h
    print("Площа бічної поверхні прямого циліндра",S)

def obempl(p,R,h):
    V=p*pow(R, 2)*h
    print("Об´єм прямого циліндра",V)