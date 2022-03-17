str='ASDFsdgsdGH'
up=0
sm=0
for i in str:
    if i.islower()==True:
        up=i.upper()
        print(up,end='')
for i in str:
    if i.isupper()==True:
        sm=i.lower()
        print(sm,end='')

