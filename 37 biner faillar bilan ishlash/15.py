fileNom='file15'
with open(fileNom+',text',mode='w') as file:
    s=0
    n=[1,2,3,4,5,6,7,8,9]
    for i in range(len(n)):
        if n[i]%2==0:
            s+=n[i]

    print(s)
