n=10
i=1
f_i=0
f_1=f_2=1
while f_i==n:
    i+=1
    f_i=f_1+f_2
    f_1=f_2
    f_2=f_i
    if n==f_i:
     print(f_1,f_i,f_i+f_i)