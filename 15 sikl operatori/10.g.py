from math import sin,cos
n=5
s=0
for i in range(1,n+1):
    s+=(cos(1)+cos(i))/(sin(1)+sin(i))
    print(s)