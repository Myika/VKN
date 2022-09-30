s1=input("Введіть перший рядок ")
s2=' '.join(f'x={word}' for word in s1.split())
print(s2)