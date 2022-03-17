def power4(n,x,a):
    s=0
    for i in range(1,n+1):
        s=(a-i+1)*x**i/i
        print(s)
power4(6,4,3)
