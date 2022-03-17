fileNom='file19'
with open(fileNom+',text','w') as file:
    str='2 4 3 4 6 5'
    str=str.split(' ')
    for i in range(len(str)-1):
        if str[i-1]<str[i]>str[i+1]:
            file.write(str[i])
            print(str[i])