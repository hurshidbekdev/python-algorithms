a=1
b=-2
c=3
print(a>0 and b<0 and c>0)



a=-1
b=-2
c=3
if a>b>0>c:
    print('true')
elif a>c>0>b:
    print('true')
elif b>a>0>c:
    print('true')
elif b>c>0>a:
    print('true')
elif c>a>0>b:
    print('true')
elif c>b>0>a:
    print('true')