fileNom='fileInt'
with open(fileNom+',text','w') as file:
    str='1 2 3 4 5 6 7'
    str=str.split(' ')
    sum=0
    for i in range(len(str)):
        sum+=int(str[i])
        print(sum)
