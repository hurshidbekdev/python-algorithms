n=[2,3,4,5,1,6,9,11,10,12]
index=0
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        index=i
        max=n[i]
print(index)
