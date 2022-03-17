with open('file9.1,text',mode='r') as file:
    a=file.read()
fileNom='file9.2'
with open(fileNom+',text',mode='w') as file:
    file.write(a[:1]+a[-1:len(a)])
    print(a[:1]+a[-1:len(a)])

