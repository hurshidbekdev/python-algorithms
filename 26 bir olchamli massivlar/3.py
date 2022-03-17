n=[1,2,3,4,5,6,7,8,9]
d=2
s=0
for i in range(len(n)):
    s=n[i]+d
print(s)

# a=[]
# n=10
# d=3
# s=2
# for i in range(1,n+1):
#     a.append(s)
#     s+=d
#     print(a)

a=[]
n=10
d=3
s=0
for i in range(1,n+1):
    a.append(s)
    s=i+d
    print(a)