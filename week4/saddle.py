def find_saddle(matrix):
    for i in range(r):
        min_val=min(matrix[i])
        min_col=matrix[i].index(min_val)
        saddle=0
        for j in range(c):
            if matrix[j][min_col]>min_val:
                saddle=0
                break
            else:
                saddle=1
    return saddle

r=int(input("Enter the number of rows : "))
c=int(input("Enter the number of columns : "))
matrix=[]
for i in range(r):
    row=list(map(int, input("Enter the row of the matrix : ").split()))
    matrix.append(row)

print(find_saddle(matrix))