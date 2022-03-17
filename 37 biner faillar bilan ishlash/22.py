fileNom='file22'
with open(fileNom+',text','w') as file:
 n=[2,1,5,4,7,6]
 temp=0
 s=str

 for i in range(len(n)):
    for j in range(len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp

            file.write(str(n))
print(str(n))






