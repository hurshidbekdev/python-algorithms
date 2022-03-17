fileNom='file2c'
with open(fileNom+',text',mode='w') as file:
    str='215678934'
    x1=max(str)
    x2=min(str)
    file.write(max(str))
    file.write(min(str))
    print(x1,x2)
