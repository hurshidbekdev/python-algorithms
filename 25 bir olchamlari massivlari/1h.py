from math import factorial
n=[]
a=10
s=0
for i in range(0,a+1):
    n.append(s)
    s=i/factorial(i)-(i+1)/factorial(i+1)
    print(n)