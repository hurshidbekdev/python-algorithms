str='dysufgvwu'
n=20
if len(str)>n:
    print(str[0:n])
else:
    for i in range(n-len(str)):
        print('.',end='')
    print(str)