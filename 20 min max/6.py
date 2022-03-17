n=[2,3,4,5,1,6,9,11,10,12]
max=n[0]
min=n[0]
indexMx=0
indexMn=0
for i in range(len(n)):
    if max<n[i]:
        indexMx=i
        max=n[i]
print(indexMx)
for i in range(len(n)):
    if min>n[i]:
        indexMn=i
        min=n[i]
print(indexMn)