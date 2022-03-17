n=[1,2,4,3,5,4,12,6,13,7,9,11,9]
for i in range(len(n)):
    if n[len(n)-1]>n[i]<n[i+1]:
        print(n[i])