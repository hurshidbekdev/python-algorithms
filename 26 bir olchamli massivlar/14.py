n=[1,2,3,4,5,6,7,8,9]
juft=[]
toq=[]
for i in n:
    if i%2==0:
        juft.append(i)
    if i%2!=0:
        toq.append(i)
print(juft[::-1]+toq[::1])


