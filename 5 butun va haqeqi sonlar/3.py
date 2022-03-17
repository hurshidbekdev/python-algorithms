import math
from math import sqrt
a=4
b=5
c=6
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
print(s,p)
print(math.ceil(s))