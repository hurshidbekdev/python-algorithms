n=[3,5,4,9,8,7,10,12,6,1,2]
index=0
for i in range(len(n)-1):
    if n[i]<n[i+1]:
        index+=1
print(index)