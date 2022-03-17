n=5
s=1
for i in range(1,n+1):
    s*=(1+1/i**2)
    print(s)