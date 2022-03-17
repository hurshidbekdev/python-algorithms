n=30
for i in range(1,n+1):
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=j
    if c==i:
        print(c)


