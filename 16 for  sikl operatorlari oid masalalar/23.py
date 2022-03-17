from math import factorial
n=9
x=4
s=0
for i in range(1,n+1,2):
    s+=(-1)**i*x**(2*i+1)/(2**i+1)
    print(s)