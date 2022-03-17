n=[1,5,3,8,7,-1,4,8]
s=1
for i in n:
    if i<0:
        break
    s*=i
    print(s)
