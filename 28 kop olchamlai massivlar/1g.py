matrix=[]
n=5
for i in range(n):
    temp=[]
    for j in range(n):
        if n-4+i>j:
            temp.append(n-i+j)
        else:
            temp.append(0)
    matrix.append(temp)
    print(matrix[i])
