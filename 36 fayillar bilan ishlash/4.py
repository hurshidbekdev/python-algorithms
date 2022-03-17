with open('file.4.1,text','r') as file:
    a=file.read()
    arr=a.split(' ')
    juft = open('juft.text','w')
    toq = open('juft.text', 'w')
    for i in range(len(arr)):
        if int(arr[i])%2==0:
            juft.write(arr[i])
        else:
            toq.write(arr[i])
    juft.close()
    toq.close()


