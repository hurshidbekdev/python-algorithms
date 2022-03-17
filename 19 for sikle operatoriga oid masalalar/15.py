n=100
foiz=20
count=0
sum=n
while sum<=2*n:
    sum+=sum*foiz/100
    count+=1
    print(count,sum)
