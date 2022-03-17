n1='abcdefg'
n2='hiklmn'
n=3
print(n1[:n]+n2[len(n2)-n])


str='hello'
for i in range(len(str)):
    print(str[i])


str='hello'
for i in str:
    print(i)


str='hello'
for i in range(len(str)):
    if str[i]=='l':
        print(i)