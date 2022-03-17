def power234(n):
    print(n**2)
    print(n ** 3)
    print(n ** 4)
power234(3)

def power(n):
    a=1
    for i in range(1,n+1):
        a*=3
        print(a)
power(4)