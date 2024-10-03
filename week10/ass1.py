para = input("Enter a string : ")
n = int(input("Enter a no. : "))
dict={}
l1=para.split()
for i in l1:
    if i not in dict:
        dict[i]=l1.count(i)
ans=0
for i,j in dict.items():
    if j==n:
        ans=1
        break
print(ans)