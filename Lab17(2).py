import pandas as pd 
import json


a=open("/Users/llirik/Desktop/Univer/Lab 17/pupils.json") 
b=a.read()
f=json.loads(b)
a.close()

df=pd.Series(f)
print(df)
print("---------")
d1=df["Іванов"]
d2=df["Марчук"]
d3=df["Гмитронь"]
d=d1,d2,d3
print(d)

df2=pd.Series(d)
print(df2)
df3=df2.T
print(df3)

df.to_json('/Users/llirik/Desktop/Univer/Lab 17/years.json')