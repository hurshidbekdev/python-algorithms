n=[2,4,5,12,4,5,6,7]
index=0
for i in range(len(n)):
    if n[i]%2!=0:
        index+=i
        print(index)
        break

