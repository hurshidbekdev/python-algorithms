n=[1,3,2,6,5,12,9,8]
min=n[0]
for i in range(len(n)):
    if min>n[i]:
        min=n[i]
print(min)