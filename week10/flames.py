import string

def remove_matching(l1,l2):
    for i in l1:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
    
p1=input("Enter 1st person name : ")
p2=input("Enter 2nd person name : ")
p1=p1.replace(" ","")
p2=p2.replace(" ","")
l1=list(p1.upper())
l2=list(p2.upper())
remove_matching(l1,l2)
print(l1,l2)
count=len(l1)+len(l2)
result=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while(len(result)>1):
    split_index=(count%len(result))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]

print(result[0])