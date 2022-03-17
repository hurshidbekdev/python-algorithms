n=7
isPrime=True
for i in range(2,n):
    if n%i==0:
        isPrime=False
if isPrime==True:
    print('tub')
else:
    print('false')