from math import cos
n=6
s=0
x=4
for i in range(1,n+1):
    s=(x+cos(x*i)/2**i)
    print(s)