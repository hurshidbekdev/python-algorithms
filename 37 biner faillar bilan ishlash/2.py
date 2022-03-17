fileNom='file.2'
with open(fileNom+',text',mode='w') as file:
    n=10
    for i in range(1,n):
        file.write(str(i))