def power(n,m):
    if m==1:
        return n
    else:
        return n+power(n,m-1)
x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
print("The product of ",x,"and",y,"is",power(x,y))
