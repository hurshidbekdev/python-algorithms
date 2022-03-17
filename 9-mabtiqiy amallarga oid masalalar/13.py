# a=1
# b=-2
# c=-3
# print(a>0 and b<0 and c<0)


a=-1
b=-2
c=3
if a>0>b>c:
    print('true')
elif a>0>c>b:
    print('true')
elif b>0>a>c:
    print('true')
elif b>0>c>a:
    print('true')
elif c>0>a>b:
    print('true')
elif c>0>b>a:
    print('true')