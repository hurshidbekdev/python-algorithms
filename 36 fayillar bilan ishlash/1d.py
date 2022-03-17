fileNom='fileD'
with open(fileNom+',text',mode='w') as file:
 str='abcdefg'
 file.write(str[-1:-2:-1])

 print(str[-1:-2:-1])
