n=[2,3,4,5,1,6,12,44,54,76,2,5]
index=1
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
        index+=1
print(index+1)
print(max)
