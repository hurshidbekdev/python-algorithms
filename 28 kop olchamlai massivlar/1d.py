matrix=[]
n=5
for i in range(n):
    temp=[]
    for j in range(n):
        if i==j:
            temp.append(i)
        else:
            temp.append(0)
    matrix.append(temp)
    print(matrix[i])