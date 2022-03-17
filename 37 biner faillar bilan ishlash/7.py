fileNom='file7'
with open(fileNom+',text',mode='w') as file:
    str='1234'
    file.write(str[:2]+str[-1:len(str):])
    print(str[:2]+str[-1:len(str)])