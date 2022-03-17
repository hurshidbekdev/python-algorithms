with open('file8.1,text',mode='r') as file:
    a=file.read()
fileNom='file8.2'
with open(fileNom+',text',mode='w') as file:
    file.write(a)