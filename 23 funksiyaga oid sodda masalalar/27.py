def power5(n):
    k=1
    a=25
    for i in range(n):
        k*=5
    if k==a:
        print('true')
    else:
        print('false')
power5(2)