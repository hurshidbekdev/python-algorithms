def polindrom(n):
    k=1
    for i in range(1,n+1):
        k+=1
        if k%2==0:
            print(f'{i}=true')
        else:
            print('false')
polindrom(5)


