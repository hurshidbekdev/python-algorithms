def tub(n):
    isi=True
    for i in range(2,n):
        if n%i==0:
            isi=False
    if isi==True:
        print('yes')
    else:
        print('no')
tub(7)
