
with open('file5,text',mode='r') as file:
    a=file.read()
    c=0
    for i in range(len(a)):
        if a[i]:
         c+=1
         print(c)
        else:
            print('no')

