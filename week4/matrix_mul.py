def transpose(matrix):
    r=len(matrix)
    c=len(matrix[0])
    mat_trans=[[matrix[j][i] for j in range(r)] for i in range(c)]
    return mat_trans

def mul(matrix,scalar):
    r=len(matrix)
    c=len(matrix[0])
    trans_mat=transpose(matrix)
    mat_mul=[]
    for i in trans_mat:
        row= [scalar * j for j in i] 
        mat_mul.append(row)
    return mat_mul

r=int(input("Enter the number of rows : "))
c=int(input("Enter the number of columns : "))
matrix=[]
for i in range(r):
    row=list(map(int, input("Enter the row of the matrix : ").split()))
    matrix.append(row)
scalar=int(input("Enter the scalar value : "))
res=mul(matrix,scalar)
for val in res:
    print(" ".join(map(str, val)))