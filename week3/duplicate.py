numbers = input("Enter the numbers :")
list1 = numbers.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
unique = []
for i in list1:
    if i not in unique:
        unique.append(i)
for i in unique:
    print(i,end=" ")