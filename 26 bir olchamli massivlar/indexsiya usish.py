n=[6,4,7,9,1,2,10,11,15,12,13]
print(sorted(n))
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)