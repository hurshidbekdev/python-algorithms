n=[1,2,4,6,1,4,12,13,3,5,9,15,141]
k=[]
a=0
for i in n:
    k.append(i)
    a=sorted(k)
for i in range(1,len(a)-1):
    if a[i]<a[i+1]:
         print(a[i])

n=[1,2,4,6,2,4,12,13,3,5,9,11]
for i in range(1,len(n)-1):
    if n[i]<n[i+1]:
     print(n[i])