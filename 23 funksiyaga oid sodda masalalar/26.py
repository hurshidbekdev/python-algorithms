def power5(k):
    a=1
    n=25
    for i in range(k):
        a*=5
    if a==n:
        print('true')
    else:
        print('false')
power5(3)
