from math import sqrt
a=2
b=10
c=6
d=b**2-4*a*c
x_1=-b+sqrt(d)
x_2=-b-sqrt(d)
if x_1>x_2:
    print(True)
else:
    print(False)
