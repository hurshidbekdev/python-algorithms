n=[1,3,7,6,8,4,2]
# print(sorted(n))
for i in  range(len(n)):
    for j in range(len(n)):
        if n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)