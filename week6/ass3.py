def non_decreasing(L):
    if len(L)<=1:
        return True
    if L[0]>L[1]:
        return False
    else:
        return non_decreasing(L[1:])
    
L=list(map(int, input("Enter the list: ").split()))
print(non_decreasing(L))
