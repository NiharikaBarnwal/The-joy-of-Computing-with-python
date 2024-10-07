def checkNum(num):
    iteration = 0
    while(num!=1):
        if num%2==0:
            num=int(num/2)
        else:
            num=(num*3)+1
        iteration+=1
    print(iteration,end="")

x=int(input())
checkNum(x)