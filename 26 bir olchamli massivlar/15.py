n=[1,2,3,4,5,6,7,8,9,10]
pair=[]
odd=[]
for i in n:
    if i%2==0:
        pair.append(i)
    if i%2!=0:
        odd.append(i)
print(odd[::1]+pair[::-1])