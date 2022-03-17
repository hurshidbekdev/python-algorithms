k=10
i=2
a_i=0
a_1=2
while i<k:
    i+=1
    a_i=a_1+1/a_1
    a_1=a_i
    print(a_i)
