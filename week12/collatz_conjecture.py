def checkNum(num):
    x=num
    iteration = 1
    while(num!=1):
        if num%2==0:
            num=int(num/2)
        else:
            num=(num*3)+1
        iteration+=1
    print(x,iteration)

for i in range(200,3000):
    checkNum(i)