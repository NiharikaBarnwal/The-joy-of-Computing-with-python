def merge_list(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1
    return res

a=list(map(int, input("Enter 1st list : ").split()))
b=list(map(int, input("Enter 2nd list : ").split()))
res=merge_list(a,b)
for i in res:
    print(i,end=' ')