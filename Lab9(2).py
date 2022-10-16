a=[]
b=[]
c=[]
for i in range(1, 201, 1):
    if i % 4==0:
        a.append(i)
    if i % 3==0:
        b.append(i)
    if i % 5==0:
        c.append(i)
##A
a_temp=[]
b_temp=[]
c_temp=[]
for j in range(0, len(a), 1):
    if a[j]%12==0:
        a_temp.append(a[j])
        
    if a[j]%20==0 and a[j] %3 !=0:
        b_temp.append(a[j])
    if a[j]%15==0 and a[j] %4 !=0:
        c_temp.append(a[j])
print("A")
print("Ділиться на 12",a_temp)
print("Ділиться на 20 і не ділиться на 3",b_temp)
print("Ділиться на 15 і не ділиться на 4",c_temp)
##B
a_temp.clear()
b_temp.clear()
c_temp.clear()
for j in range(0, len(b), 1):
    if b[j]%12==0:
        a_temp.append(b[j])
    if b[j]%20==0 and b[j] %3 !=0:
        b_temp.append(b[j])
    if b[j]%15==0 and b[j] %4 !=0:
        c_temp.append(b[j])
print("B")
print("Ділиться на 12",a_temp)
print("Ділиться на 20 і не ділиться на 3",b_temp)
print("Ділиться на 15 і не ділиться на 4",c_temp)
##C
a_temp.clear()
b_temp.clear()
c_temp.clear()
for j in range(0, len(c), 1):
    if c[j]%12==0:
        a_temp.append(c[j])
    if c[j]%20==0 and c[j] %3 !=0:
        b_temp.append(c[j])
    if c[j]%15==0 and c[j] %4 !=0:
        c_temp.append(c[j])
print("C")
print("Ділиться на 12",a_temp)
print("Ділиться на 20 і не ділиться на 3",b_temp)
print("Ділиться на 15 і не ділиться на 4",c_temp)  
