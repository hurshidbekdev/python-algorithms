n=[2,1,3,4,5,6,12,44,54,76]
b=12
index=0
for i in range(len(n)):
    if n[i]>b:
        index+=i
        print(index)
        break
