fileNom='file11'
with open(fileNom+',text',mode='w') as file:
    str='1 2 3 4 5 6 7 8 9'
    x=str.split(' ')
    juft = open('juft,text11','w')
    toq = open('toq,text11', 'w')
    for i in range(len(x)):
        if i%2==0:
            juft.write(x[i])
        else:
            toq.write(x[i])




