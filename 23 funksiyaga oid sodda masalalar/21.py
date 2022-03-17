def sum(a,b):
    s=0
    for i in range(a,b+1):
        s+=i
    print(s)
sum(2,8)

def sumRange(a,b,c):
    c1=0
    c2=0
    for i in range(a,b+1):
        c1+=i
    for j in range(b,c+1):
        c2+=j
    print(c1+c2)
sumRange(1,5,9)
