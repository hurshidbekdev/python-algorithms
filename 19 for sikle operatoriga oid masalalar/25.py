n=10
i=1
f_1=f_2=1
f_i=0
while i<n:
    i+=1
    f_i=f_1+f_2
    f_1=f_2
    f_2=f_i
    print(f_i)
    break