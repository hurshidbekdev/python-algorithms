n=[2,3,4,3,5,4,12,6,13,7,9,11,9]
for i in range(1,len(n)-1):
    if n[i-1]>n[i]<n[i+1]:
        print(n[i])

