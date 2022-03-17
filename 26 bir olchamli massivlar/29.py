n=[1,2,4,3,5,4,12,6,13,7,8,9]
a=sorted(n)
k=[]
for i in n:
    if i%2!=0:
        k.append(i)
print(min(k))
