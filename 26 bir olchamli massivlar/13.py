n=[1,2,3,4,5,6,7,8,9]
a=10
s=0
k=[]
for i in n:
    if i%2!=0:
        s=a-i
        k.append(s)
print(k)

# k=[]
# n=10
# s=0
# for i in range(1,n+1):
#     if i%2!=0:
#         s=n-i
#
#         k.append(s)
#     # s=n-i
# print(k)
