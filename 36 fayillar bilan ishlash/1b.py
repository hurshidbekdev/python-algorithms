fileNom='fileB'
with open(fileNom+',text',mode='w') as file:
    a = 5
    b = 4
    print(file.write(str(a * b)))

