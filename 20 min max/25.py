n=[1,2,3,4,5,6,7,8,9,10]
arr=[]
for i in range(0,len(n)-1,2):
    arr.append(n[i]*n[i+1])
print(min(arr))
