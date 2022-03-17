n=30
s=0
for i in range(1,n+1):
    isi=True
    for j in range(2,i):
        if i%j==0:
            isi=False
    if isi==True:
        s+=1
        print('yes',i)

