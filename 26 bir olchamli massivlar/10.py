
n=[1,4,3,2,8,7,9,5,16,15,11,12,13]
juft =[]
toq=[]
n=sorted(n)
for i in n:
    if i%2==0:
        juft.append(i)
for i in n:
    if i%2!=0:
        toq.append(i)
print(juft+toq[::-1])












