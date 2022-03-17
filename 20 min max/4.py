n=[2,3,4,5,1,6,9]
min=n[0]
index=0
for i in range(len(n)):
    if min>n[i]:
        index=i
        min=n[i]
print(index)



