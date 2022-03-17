n=[2,3,4,5,1,6,12,44,54,76]
index=0
min=n[0]
for i in range(len(n)):
    if min<n[i]:
        min=n[i]
        index+=i
        print(index)
print(min)











