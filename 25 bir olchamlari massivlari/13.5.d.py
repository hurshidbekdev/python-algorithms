n=[1,3,5,7,11,9]
min=n[0]
for i in range(len(n)):
    if min>n[i]:
        min=n[i]
print(min)