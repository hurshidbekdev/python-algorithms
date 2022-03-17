from math import factorial
n=5
x=4
s=0
for i in range(0,n+1):
    s+=x**i/factorial(i)
    print(s)
