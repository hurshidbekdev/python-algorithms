n=[3,5,4,9,8,7,10,12,6,1,2,4]
arr=[]
for i in range(0,len(n)-1,2):
    arr.append(n[i]+n[i+1])
print(max(arr))
