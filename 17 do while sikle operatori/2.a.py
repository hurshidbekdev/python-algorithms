from math import factorial
n=5
x=3
s=0
for i in range(1,n+1):
    s+=x**i/factorial(i)
    print(s)