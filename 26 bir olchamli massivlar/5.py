# n=[1,2,3,4,5,6,7,8,9]
# f0=f1=1
# f2=0
# for i in range(len(n)):
#     f2=f0+f1
#     f0=f1
#     f1=f2
#     print(f2)
a=[]
n=10
f0=f1=1
f2=0
for i in range(1,n+1):
    a.append(f2)
    f2=f0+f1
    f0=f1
    f1=f2
print(a)
