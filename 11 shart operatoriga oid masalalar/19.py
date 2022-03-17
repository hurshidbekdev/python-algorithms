a=3
b=3
c=2
d=3
if a>=b>=d<c:
    print(c)
elif b>=c>=d<a:
    print(a)
elif a>=c>=d<b:
    print(b)
elif a>=b>=d>c:
    print(c)
elif b>=c>=d>a:
    print(a)
elif a>=c>=d>b:
    print(b)
elif a>=b>=c>d:
    print(d)
elif a>=b>=c<d:
    print(d)