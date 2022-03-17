# n=[1,-2,3,-4,5,6,-7,8,9]
# flag=True
# for i in range(0,len(n),2):
#     if n[i]>0 and n[i]<0:
#         pass
#     else:
#         flag=False
# print('togri' if flag else 'hato')


n=[1,-2,3,-4,5,6,-7,8,9]
mus=[]
man=[]

for i in n:
    if  i<0:
        man.append(i)
    if i>0:
        mus.append(i)


print(mus+man)


