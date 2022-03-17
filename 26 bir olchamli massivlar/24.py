n=[3,6,9,12,15,18,21]
d=n[1]-n[0]
count=0
for i in range(len(n)):
    if d==n[i]-n[i-1]:
        count+=1
print(count)
if count==len(n):
     print(d)
else:
    print(0)

