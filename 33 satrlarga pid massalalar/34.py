s1='ab1sfd1cb1d'
s2='1'
arr=[]
index=s1[::-1].find(s2)
print(index)
for i in range(len(s1)):
    arr.append(s1[i])
print(arr.pop(len(arr)-index-1))
print(arr)

