n=[1,4,5,8,9,3,2]
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)
