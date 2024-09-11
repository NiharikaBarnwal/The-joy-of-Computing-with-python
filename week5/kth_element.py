def kth_element(a,k):
    n=len(a)
    a.sort()
    mid=(n-1)//2
    if a[k-1]==a[-k] and (k==mid+1 or n-k==mid):
        return 1
    elif a[k-1]==a[-k]:
        return-1
    else:
        return 0

a=list(map(int, input("Enter 1st list : ").split()))
k=int(input("Enter the kth position : "))
res=kth_element(a,k)
print(res)