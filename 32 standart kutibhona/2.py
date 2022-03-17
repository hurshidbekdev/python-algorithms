# str='fr$fg$er$e'
# c=0
# for i in str:
#     if i=='$':
#         c+=1
# print(c)


str='sa.id.ud.w'
c=0
s=0
for i in str:
    if i=='.':
        c+=1
    if i=='%':
        s+=1
print(c,s)
