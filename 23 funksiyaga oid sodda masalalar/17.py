from math import  sqrt
def pow(a,b,c):
    d=b**2-4*a*c
    x1=-b+sqrt(d)
    x2 = -b-sqrt(d)
    print(x1,x2)
pow(2,8,3)