def skew(matrix):
    r=len(matrix)
    skew=1
    for i in range(r):
        for j in range(r):
            if matrix[i][j]!=-matrix[j][i]:
                skew=0
    return skew


r=int(input("Enter the number of rows : "))
matrix=[]
for i in range(r):
    row=list(map(int, input("Enter the row of the matrix : ").split()))
    matrix.append(row)
print(skew(matrix))