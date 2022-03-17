fileNom='file10'
with open(fileNom+',text',mode='w') as file:
    str='123456'
    file.write(str[::-1])
    print(str[::-1])