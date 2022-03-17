n=10
a=1
f1=0
f2=1
while a<n:
    a+=1
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)