arr=[1,2,3,4,6]
arr.sort()
target=5
index=0
for i in range(len(arr)-1):
    if arr[i]<=target<=arr[i+1]:
        index=i
        break
newArr=[0,0,0,0,0,0,0,0,0,]
print(arr)
print(index)
count=0
for i in range(0,len(arr)+1):
    if index != i:
        newArr[i]=arr[count]
        count+=1
        print(newArr)

