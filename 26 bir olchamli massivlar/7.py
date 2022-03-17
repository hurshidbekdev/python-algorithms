n=[1,2,3,4,5,6,7,8,9]
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)

n=[1,2,3,4,5,6,7,8,9]
print(n[::-1])

