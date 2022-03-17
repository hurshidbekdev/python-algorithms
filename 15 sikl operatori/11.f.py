from math import factorial
n=5
s=1
for i in range(2,n+1):
    s*=(1+1/factorial(i))**2
    print(s)