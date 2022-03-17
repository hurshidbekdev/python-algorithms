s='cbchcbiuefb'
for i in range(len(s)):
    if s[i]=='c':
        print(s[i]*2,end='')

s='cbchcbiuefb'
for i in s:
    if i=='c':
        print(i*2)


s='cbchcbiuefb'
print(s.replace('c','2c'))