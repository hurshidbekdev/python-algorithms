fileNom='fileC'
with open(fileNom+',text',mode='w') as file:
    a=4
    b=3
    file.write(str(a**2+b**2))
    print(a**2+b**2)
