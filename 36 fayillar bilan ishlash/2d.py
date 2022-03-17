fileNom='file2d'
with open(fileNom+',text',mode='w') as file:
    str='236589'
    max=str
    min=min(str)
    for i in range(len(str)):
        if max<str[i]:
            max=str[i]
    file.write(max)
    file.write(min)

    print(max,min)
