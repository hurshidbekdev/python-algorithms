a_1=1
a_2=2
a_i=0
n=10
i=0
while i<n:
    i+=1
    a_i=(a_1+2*a_2)/3
    a_1=a_2
    a_2=a_i
    print(a_i)
    break
