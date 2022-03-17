num=[1,2,11,3,15,4,5,18,6,7,8,9]
k=2
l=6
s=0
c=0
count=0
count1=0
count2=0
for i in range(k,l):
    s+=num[i]
    count+=1
for i in num:
    c+=i
    count1+=1
count2=(count1-count)
print((c-s)/count2)





