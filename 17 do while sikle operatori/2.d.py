from math import sin,factorial
n=6
s=1
x=4
for i in range(1,n+1):
    s*=(1+sin(i*x)/factorial(i))
    print(s)