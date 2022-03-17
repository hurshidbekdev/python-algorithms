# n=[1,3,4,5,6,2,8]
# s=0
# for i in range(len(n)):
#     s=2**i+3**(i+1)
#     print(s)


n=10
a=[]
s=0
for i in range(1,n+1):
    a.append(s)
    s = 2 ** i + 3 ** (i + 1)
    print(a)