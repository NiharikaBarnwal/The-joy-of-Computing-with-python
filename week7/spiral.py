import turtle
from random import randint

turtle.bgcolor("black")
seurat=turtle.Turtle()
width = 5
height = 7
seurat.penup()
list_color = ["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
dot_distance = 25
seurat.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    col = randint(0,11)
    seurat.color(list_color[col])
    '''
    m=index of ending row
    n=index of ending column
    k=index of starting row
    l=index of starting column
    '''
    while k<m and l<n:
        if(f==1):
            seurat.right(90)
        # printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        col = randint(0,10)
        seurat.color(list_color[col])
        k+=1
        f=1
        seurat.right(90)
        # Printing the last column from the remaining columns
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[i][n-1],end=" ")
        col = randint(0,10)
        seurat.color(list_color[col])
        n-=1
        seurat.right(90)
        if k<m:
            # Printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[m-1][i],end=' ')
            m-=1
        col = randint(0,10)
        seurat.color(list_color[col])
        seurat.right(90)
        if l<n:
            # Printing the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[i][l],end=' ')
            l+=1
        col = randint(0,10)
        seurat.color(list_color[col])

# a=[]
# count=1
# for i in range(4):
#     l=[]
#     for j in range(4):
#         l.append(count)
#         count+=1
#     a.append(l)

spiral(20,20)
turtle.done