with open('minimum,text',mode='r') as file:
    a=file.read()
    a=a.split(' ')
    min=int(a[0])
    for i in range(0,len(a),2):
        if min > int(a[i]):
            min = int(a[i])
    print(min)