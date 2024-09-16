def check_binary(mat):
    for row in mat:
        for element in row:
            if element not in [0,1]:
                return False
    return True
    
def check_symmetric(mat,r,c):
    for i in range(r):
        for j in range(c):
            if mat[i][j]!=mat[j][i]:
                return False
    return True

r=int(input("Enter the number of row : "))
c=int(input("Enter the number of col : "))
matrix=[]
for i in range(r):
    row=list(map(int,input("Enter the row elements : ").split()))
    matrix.append(row)

binary=check_binary(matrix)
symmetry=check_symmetric(matrix,r,c)
if binary and symmetry:
    print('11')
elif binary and not symmetry:
    print('10')
elif not binary and symmetry:
    print('01')
else:
    print('00')