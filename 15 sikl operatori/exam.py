# # n=7
# # s=0
# # for i in range(1,n):
# #     if n%i==0:
# #         s+=i
# # if s==n:
# #     print('tub')
# # else:
# #     print('emas')
#
#
# # n=30
# #
# # for i in range(1,n):
# #     s=0
# #     for j in range(1,i):
# #         if i%j==0:
# #          s+=j
# #     if s==i:
# #       print(s)
#
#
# n=7
# isi=True
# for i in range(2,n):
#         if n%i==0:
#          isi=False
# if isi==True:
#     print('tub')
# else:
#     print('yoq')


n=6
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print('yes')


n=30
for i in range(1,n+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(s)


# n=7
# isi=True
# for i in range(2,n):
#     if n%i==0:
#         isi=False
# if isi==True:
#     print('yes')


n=30
for i in range(1,n+1):
    isi=True
    for j in range(2,i):
        if i%j==0:
            isi=False
    if isi==True:
        print(i)





