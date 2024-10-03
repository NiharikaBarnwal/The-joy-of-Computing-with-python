str1 = input("Enter the string : ")
l1=str1.split()
lst=[]
for i in l1:
    l2=i.split(".")
    lst.append(l2)
count=0
for i in lst:
    if len(i[1])>len(i[0]):
        count+=1
print(count)