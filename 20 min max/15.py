n=[2,1,3,4,5,6,12,45,44,54,76]
index=0
a=3
c=54
temp=[]
for i in range(len(n)):
    if a<n[i]<c:
        temp.append(n[i])
        index+=i
print(max(temp))
