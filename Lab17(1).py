import pandas as pd
import csv
import numpy as np

masiv=[]
with open('/Users/llirik/Desktop/Univer/Lab 17/matrix.csv', 'r', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         a=', '.join(row)
         masiv.append(a)


df=pd.Series(masiv)
df1=df.T
print(df1.sum())
f = open('/Users/llirik/Desktop/Univer/Lab 17/suma.txt', 'w')
for index in df1:
    f.write(index + '\n')
f.close()