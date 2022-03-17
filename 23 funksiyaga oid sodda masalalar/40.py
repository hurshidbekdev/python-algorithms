from math import factorial
def pow(n,x):
    s=0
    for i in range(0,n+1):
        s+=x**i/factorial(i)
        print(s)
pow(6,2)

