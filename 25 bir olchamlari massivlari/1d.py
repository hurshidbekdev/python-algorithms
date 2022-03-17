from math import fabs
n=[]
a=8
s=1
for i in range(1,a+1):
    s*=fabs(i)
    n.append(s)
    print(n)

# n=[2,3,4,5,6,7,8,9]
# s=1
# for i in range(len(n)):
#     s=fabs(n[i])
#     print(s)