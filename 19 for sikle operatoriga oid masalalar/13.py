n=20
s=0
t=2
i=1
count=0
while i<n:
    i+=1
    s+=1/i
    count+=1
    if s>t:
     print(count)
     break