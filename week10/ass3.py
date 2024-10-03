str1 = input("Enter a string : ")
l1=list(map(int,str1.split()))
lhs=0
for i in range(len(l1)//2):
    lhs+=l1[i]
rhs=0
for i in range(len(l1)//2,len(l1)):
    rhs+=l1[i]
if lhs>rhs:
    print(-1)
elif lhs<rhs:
    print(1)
else:
    print(0)