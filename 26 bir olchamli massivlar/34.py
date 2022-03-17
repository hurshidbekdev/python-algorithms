n=[1,3,2,4,6,5,7,9,8]
lokalmax=0
for i in range(1,len(n)-1):
    if n[i-1]<n[i]>n[i+1]:
        lokalmax=[i]
        print(lokalmax)
