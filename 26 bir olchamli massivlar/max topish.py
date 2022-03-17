n=[2,5,8,6,3,19,9]
max=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
print(max)