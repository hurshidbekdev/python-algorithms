def pow(a,n):
    a=1
    for i in range(0,n+1):
        a=2**i
        if a>0:
            print(a)
        else:
            print(0)

pow(2,4)