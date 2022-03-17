n='egr*tjr*fig*'
c=0
for i in range(len(n)):
    if n[i]=='*':
        c+=1
print(c,f'{n[i]}')