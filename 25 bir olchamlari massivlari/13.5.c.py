n=[2,4,6,8,12,10,14]
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
print(max)