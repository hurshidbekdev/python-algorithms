n='ed+r+fv+ss*ju*'
c1=0
c2=0
for i in range(len(n)):
    if n[i]=='+':
        c1+=1
print(c1)
for i in range(len(n)):
    if n[i]=='*':
        c2+=1
print(c2)