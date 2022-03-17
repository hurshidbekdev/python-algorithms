n='ed+r+fv+s-s*---ju*'
c1=0
c2=0
c3=0
for i in range(len(n)):
    if n[i]=='+':
        c1+=1
print(c1)
for i in range(len(n)):
    if n[i]=='*':
        c2+=1
print(c2)

for i in range(len(n)):
    if n[i]=='-':
        c3+=1
print(c3)
print(f'+={c1},*={c2},-={c3}')