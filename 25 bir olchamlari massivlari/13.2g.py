n=10
s=1
a=[]
for i in range(1,n+1):
    a.append(s)
    s=2**(i+1)
    print(a)

#
# n=[1,3,3,4,5,6,7]
# s=0
# for i in n:
#     s=2**(i+1)
#     print(s)