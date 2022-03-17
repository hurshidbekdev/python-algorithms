with open('file12,text',mode='r') as file:
    a=file.read()
    x=a.split(' ')
    juft=open('juft,text12','w')
    toq = open('toq,text12', 'w')
    for i in range(len(x)):
        if i%2==0:
            juft.write(x[i])
        else:
            toq.write(x[i])
