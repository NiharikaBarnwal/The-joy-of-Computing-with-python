def magic_square(n):
    sq=[[0 for i in range(n)]for j in range(n)]
    p=n//2
    q=n-1
    i=1
    while (i<=n*n):
        if p==-1 and q==n:
            p=0
            q=n-2
        elif p==-1:
            p=n-1
        elif q==n:
            q=0
        if sq[p][q]!=0:
            p=p+1
            q=q-2
            continue
        else:
            sq[p][q]=i
        p=p-1
        q=q+1
        i=i+1

    for i in range(n):
        for j in range(n):
            print(sq[i][j],end=' ')
        print()
    print("The sum of each row/column/diagonal is: ",str(n*(n**2+1)/2))


n=int(input("Enter the size of magic square : "))
magic_square(n)