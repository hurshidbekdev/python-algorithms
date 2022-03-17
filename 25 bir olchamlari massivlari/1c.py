from math import fabs
# n=[2,3,-4,-5,9,8,-7]
# s=0
# for i in range(len(n)):
#     s=fabs(n[i])
#     print(s)

n=[]
s=0
a=10
for i in range(1,a+1):
    s+=fabs(i)
    n.append(s)
    print(n)