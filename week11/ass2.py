str1=input("Enter the sequence: ")
l1=list(map(int,str1.split(":")))
lar=max(l1)
for i in range(1,lar):
    count=0
    for x in l1:
        if x%i==0:
            count+=1
    if count==len(l1):
        print(i,end=" ")