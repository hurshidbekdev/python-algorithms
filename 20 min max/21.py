n=[3,5,4,9,8,7,10,12,6,1,2]
index=0
for i in range(len(n)-1):
    if n[i-1]<n[i]<n[i+1]:
        print(n[i])