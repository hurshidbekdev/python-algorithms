fileNom='file2a'
with open(fileNom+',text',mode='w') as file:
    str='871923'
    max=str
    for i in range(len(str)):
        if max<str[i]:
            max=str[i]
    file.write(max)
    print(max)