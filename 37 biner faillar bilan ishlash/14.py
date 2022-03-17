fileNom='file14'
with open(fileNom+',text',mode='w') as file:
    n=[1,2,3,4,5,6,7,8,9]
    s=0
    count=0
    for i in range(len(n)):
        s+=n[i]
        count+=1
        file.write(str(s/count))
        print(s/count)








