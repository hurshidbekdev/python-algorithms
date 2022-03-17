n=9
x=4
s=0
p=1
for i in range(2,n+1,2):
    p*=i
    s+=(2*i-1)*x**(2*i)/p*(2*i)*(2*i)
    print(s)