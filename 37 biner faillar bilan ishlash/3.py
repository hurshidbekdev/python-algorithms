fileNom='file3'
with open(fileNom+',text', mode='w') as file:
    n=10
    d=3
    a=2
    s=0
    for i in range(1,n):
        s=a+i*d
        file.write(str(s))