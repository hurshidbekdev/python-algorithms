from math import factorial
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=factorial(i)
        print(p)
fact(5)