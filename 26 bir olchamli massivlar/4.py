# n=[1,2,3,4,5,6,7,8,9]
# d=2
# s=1
# for i in range(len(n)):
#     s=n[i]*d
#     print(s)


n=10
a=[]
f0=f1=1
fi=0
for i in range(1,n+1):
    fi=f0+f1
    f0=f1
    f1=fi

    print(fi)


