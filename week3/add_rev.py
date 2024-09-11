numbers = input("Enter the numbers :")
list1 = numbers.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
orig=list1.copy()
list1.reverse()
final=[]
for i in range(len(list1)):
    if i%2==0:
        final.append(orig[i])
    else:
        x=orig[i]+list1[i]
        final.append(x)
for i in final:
    print(i,end=" ")