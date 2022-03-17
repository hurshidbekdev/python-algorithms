n=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(n)//2,2):
    print(n[i],n[i+1],n[len(n)-1-i],n[len(n)-2-i],end='')