fileNom='file21'
with open(fileNom+',text',mode='w') as file:
    str='1 3 2 10 1 11 8 9 7 3 5 4 4 6 5 7 '
    str=str.split(' ')

    for i in range(len(str)-1):
        if str[i-1]<str[i]>str[i+1]:
            print((str[i]))
