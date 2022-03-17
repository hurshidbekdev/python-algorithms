matrix=[]
n=5
for i in range(n):
    temp=[]
    for j in range(n):
        if i==j:
            temp.append(j+1)
        elif n-i-1==j:
            temp.append(n-i)
        else:
            temp.append(0)
    matrix.append(temp)
    print(matrix[i])