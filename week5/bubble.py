def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=[5,1,4,2,8]
bubble(a)
for i in a:
    print(i)