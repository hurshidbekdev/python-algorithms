n=[19,18,8,6,7,1,21,13,15,23]
for i in range(len(n)):
    if n[0]<n[i]<n[-1]:
        print(n[i])
        break
