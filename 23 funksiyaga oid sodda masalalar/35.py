def fac2(n):
    p1=1
    for i in range(1,n+1):
        p1*=i

    p2=1
    for i in range(1,p1+1):
        p2*=i
    return p2
print(fac2(4))
