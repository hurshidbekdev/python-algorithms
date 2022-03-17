n=9
x=4
s=0
p=1
for i in range(2,n+1,1):
    s+=(-1)**(i-1)*x**i/i
    print(s)
