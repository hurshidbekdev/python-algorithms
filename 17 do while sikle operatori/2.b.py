from math import sqrt,fabs,factorial
n=6
s=0
x=4
for i in range(1,n+1):
    s=(1/factorial(i)+sqrt(fabs(x)))
    print(s)
