def log(x):
    if x==1:
        return 0
    else:
        return 1+log(x//2)
    
x=int(input("Enter a number : "))
print(log(x))