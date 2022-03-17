n=10
u1=u2=1
u3=0
a=[]
for i in range(1,n+1):
    a.append(u3)
    u3=u1+u2
    u1=u2
    u2=u3
print(a)