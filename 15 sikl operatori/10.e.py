n=6
s=0
for i in range(2,n+1,2):
    s+=(3*(i-1)+3*(i)**1/(n-i))**(n-i)
    print(s)