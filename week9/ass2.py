string = list(input().split(" "))

def word_length(string):
    sum=0
    for i in string:
        sum+=len(i)
    avg=sum/len(string)
    if avg>4:
        return 1
    else:
        return 0
    
print(word_length(string))
