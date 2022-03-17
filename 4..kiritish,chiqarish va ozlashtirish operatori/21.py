from math import sqrt
x_1=3
x_2=6
y_1=7
y_2=9
x_3=1
y_3=5
a=x_1+y_1
b=x_2+y_2
c=x_3+y_3
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
print(s)

