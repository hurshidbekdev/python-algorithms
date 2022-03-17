str='sja,djia,l'
for i in range(len(str)-1,0,-1):
   if str[i]==',':
       break
print(str[i])