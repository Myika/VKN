from collections import Counter
import requests
from bs4 import BeautifulSoup
url=input('Введіть посилання на сторінку:')
r=requests.get(url)
res=open('/Users/llirik/Desktop/Univer/Lab 14/result.txt', 'w')
if r.status_code==200:
    wbs=BeautifulSoup(r.text,'html.parser')
    for link in wbs.find_all("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'],file=res)

elif r.status_code==404:
    print("Сторінка не доступна", file=res)
