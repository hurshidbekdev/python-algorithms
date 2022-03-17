def pow(n,x):
    s=0
    for i in  range(1,n+1):
        s=(-1)**i*x**(i+1)/(n+1)
        print(s)
pow(5,6)