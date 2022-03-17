n=[1,-2,3,-4,5,-6,7,-8,9]
flag=True
index=0
for i in range(0,len(n)-1,2):
    if not(n[i]>0 and n[i+1]<0):
        flag=False
        index=n[i]
        break
print(0 if flag else index)









