n=[2,4,3,1,5]
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
print(max)