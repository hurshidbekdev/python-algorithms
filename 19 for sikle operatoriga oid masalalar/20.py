n=10
i=0
s=0
p=0
while i<n:
    i+=1
    s=n%i
    p=n//i
    if s==2 and p==2:
     print('yes')
     break
    else:
        print('no')
        break

