with open('file6,text',mode='r') as file:
    k='7'
    a=file.read()
    x=a.split(' ').count('7')
    if x>0:
        print('yes')
    else:
        print('no')

