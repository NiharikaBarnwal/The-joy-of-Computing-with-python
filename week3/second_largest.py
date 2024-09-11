numbers = input("Enter the numbers :")
list1 = numbers.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
list1.sort()
list1.reverse()
print(list1[1])