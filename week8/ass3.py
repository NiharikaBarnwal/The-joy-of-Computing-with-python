l1=list(map(int,input().split()))
k=int(input("Enter a number : "))
l2=[k* num for num in l1]
print(max(l2))