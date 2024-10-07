def check_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

n=int(input())
sum=0
for i in range(1,n+1):
    if check_prime(i):
        sum+=i
print(sum)