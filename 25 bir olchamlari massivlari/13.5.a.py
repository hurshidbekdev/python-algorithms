n=[1,3,2,6,5,12,9,8]
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
print(max)