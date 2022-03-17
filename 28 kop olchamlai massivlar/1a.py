matrix=[]
n=5
for i in range(n):
    temp=[]
    for j in range(n):
        if n-i-1==j:
            temp.append(i+1)
        else:
            temp.append(0)
    matrix.append(temp)
    print(matrix[i])
#
#
# matrix=[]
# n=5
# for i in range(n):
#     temp=[]
#     for j in range(n):
#         if i==j:
#             temp.append(1)
#         else:
#             temp.append(0)
#         matrix.append(temp)
# print(matrix)
#
#
# matrix=[]
# n=5
# for i in range(n):
#     for j in range(n):
#         print(j)