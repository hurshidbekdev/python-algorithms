n=[1,3,5,4,7,9]
index=0
for i in range(len(n)):
    if n[i]%2==0:
        index+=1
        print(index)
    else:
        print(0)
