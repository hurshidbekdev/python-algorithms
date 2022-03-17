n=5
matrix=[]
for i in range(n):
    temp=[]
    for j in range(n):
        if n-i-1==j:
            temp.append(1)
        else:
            temp.append(0)
    matrix.append(temp)
    print(matrix[i])



