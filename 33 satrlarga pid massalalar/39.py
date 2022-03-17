s1='sdgyu ! id  fe'
c=0
for i in range(len(s1)):
    if s1[i]=='!':
        c+=1
        if c==2:
            print('yyy')
        else:
            print('no')
