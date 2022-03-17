n=[1,2,3,4,5,6,7,8,9]
flag=True
for i in range(len(n)):
    if n[i]%2!=0 and n[i+1]%2==0:
        pass
    else:
        flag=False
        break
    if flag==True:
        print('yy')