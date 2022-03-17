n=[2,3,4,5,6,7,8]
a1=2
a2=3
a3=0
for i in range(len(n)):
    a3=a1+a2
    a1=a2
    a2=a3
    print(a3)

