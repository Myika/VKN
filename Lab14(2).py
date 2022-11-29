import json
import requests
from bs4 import BeautifulSoup
import re
page = requests.get('http://funium.ru/wp-content/uploads/2019/01/3700-%D0%B5%D0%BC%D0%B5%D0%B9%D0%BB-%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%BE%D0%B2-%D0%B0%D0%B2%D1%82%D0%BE%D0%BB%D1%8E%D0%B1%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9.txt')
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
text = soup.text
w1 = re.findall('gmail.com', text)
w2 = re.findall('mail.ru', text)
chastota = {}
for word in w1:
    count = chastota.get(word, 0)
    chastota[word] = count + 1
for word in w2:
    count = chastota.get(word, 0)
    chastota[word] = count + 1
print(chastota)
with open('/Users/llirik/Desktop/Univer/Lab 14/lab14.txt', 'w') as json_file:
    inf = json.dump(chastota, json_file)