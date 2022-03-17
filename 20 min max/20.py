n=[3,5,4,9,8,7,10,12,6,1,2]
index1=0
index2=0
for i in range(len(n)-1):
    if n[i-1]<n[i]>n[i+1]:
        index1+=1
    if n[i-1]>n[i]<n[i+1]:
        index2+=1
print(index1+index2)