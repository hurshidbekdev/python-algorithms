fileNom='file20'
with open(fileNom+',text','w') as file:
    str='2 4 3 4 6 5 3 2 4 3 5 2'
    str=str.split(' ')
    count1=0
    count2 = 0
    for i in range(len(str)-1):
        if str[i-1]<str[i]>str[i+1]:
            count1+=1
    print(count1+1)
    for i in range(len(str)-1):
        if str[i-1]>str[i]<str[i+1]:
            count2+=1
    print(count2+1)
