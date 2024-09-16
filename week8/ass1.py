def sum_of_tuple(n,tup):
    sum=0
    for i in range(n):
        sum=sum+tup[i][0]
    return sum

n=int(input("Enter the number of tuples : "))
l1=[]
for i in range(n):
    tuple1=tuple(map(int,input("Enter the tuples : ").split()))
    l1.append(tuple1)
print(sum_of_tuple(n,l1))