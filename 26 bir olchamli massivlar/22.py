n=[19,18,8,6,7,1,21,13,15,23]
k=2
l=7
s=0
c=0
for i in range(k,l):
    s+=n[i]
for i in n:
    c+=i
print(c-s)

