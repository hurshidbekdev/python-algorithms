def digit(k,n):
    a=1
    for i in range(n):
        a*=2
        if k==i:
            print(k)
        else:
            print('no')
digit(4,5)