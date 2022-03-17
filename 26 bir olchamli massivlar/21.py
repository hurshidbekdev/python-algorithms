n=[19,18,8,6,7,1,21,13,15,23]
k=2
l=7
s=0
c=0
for i in n[k:l:1]:
    s+=i
    c+=1
print(s/c)