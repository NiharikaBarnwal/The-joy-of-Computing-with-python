n=int(input())
m=0
for i in range(3):
    x=round(0.3*n)
    y=round(0.7*n)
    a=round(0.5*m)
    b=round(0.5*m)
    n=x+a
    m=y+b
print(n,m)