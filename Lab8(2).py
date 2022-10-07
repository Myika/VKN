import random
import math
import numpy as np
from numpy import*
m=int(input("Введіть M "))
n=int(input("Введіть N "))
masiv1=np.zeros((m,n))
masiv2=np.zeros((m,n))
masiv3=np.zeros((m,n))
for i in range(m):
    for j in range (n):
        masiv1[i][j]=random.randint(1,30)
        masiv2[i][j]=random.randint(31,50)
        masiv3[i][j]=masiv1[i][j]+masiv2[i][j]
print("Масив А")
print(masiv1)
print("Масив В")
print(masiv2)
print("Масив С")
print(masiv3)
masiv=np.zeros((n))
for j in range (n):
    for i in range (m):
        masiv[j]=masiv[j]+masiv3[i][j]
print("суми стовб",masiv)
min=0
for i in range (n-1):
    if masiv[i]>masiv[i+1]:
        min=masiv[i+1]
print("Min",min)