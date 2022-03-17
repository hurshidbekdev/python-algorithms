str='wn!he!di!dj'
print(str.replace('!','.'))
arr=[]
for i in range(len(str)):
    arr.append(str[i])
    if arr[i]=='!':
        arr[i]='.'
print(arr)
