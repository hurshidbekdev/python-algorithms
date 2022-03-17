with open('file13,text',mode='r') as  file:
    a=file.read()
    x=a.split(' ')
    musb=open('musb13,text','w')
    man = open('man13,text', 'w')
    for i in range(len(x)):
        if i>0:
            musb.write(x[i])
        else:
            man.write(x[i])
