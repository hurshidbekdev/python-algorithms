from math import sin
n=1
x=0.1
p=1
while x<n:
    x+=0.1
    p*=(1+sin(x))
    print(p)
