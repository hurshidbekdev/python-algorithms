n=[2,4,3,1,11,5,8,7,6]
temp=0
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n[i]+n[i-1])


