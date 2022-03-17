from math import factorial
# n=[1,3,3,3,5,4]
# p=1
# for i in range(len(n)):
#     p=factorial(n[i])
#     print(p)


n=10
a=[]
s=0
for i in range(1,n+1):
    a.append(s)
    s=factorial(i)
    print(s)