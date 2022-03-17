a_1=1
a_2=2
a_i=0
i=3
n=10
while i<n:
    i+=1
    a_i=(a_1+a_2*2)/3
    a_1=a_2
    a_2=a_i
    print(a_i)