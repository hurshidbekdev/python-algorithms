n=[1,-2,3,-4,5,-6,7,-8,9]
flag=True
c1=0
c2=0
k1=[]
k2=[]
for i in n:
    c1=i
    if c1<0:
        k1.append(c1)
for j in n:
    c2=j
    if c2>0:
        k2.append(c2)
print(k1+k2)