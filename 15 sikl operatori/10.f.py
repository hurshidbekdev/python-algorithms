from math import sin
n=5
s=0
for i in range(1,n+1):
    s+=1/(sin(1)+sin(i))
    print(s)