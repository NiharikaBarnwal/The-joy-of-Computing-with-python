def is_palindrome(s):
    if len(s)==0 or len(s)==1:
        return 1
    if s[0]!=s[len(s)-1]:
        return 0
    else:
        return is_palindrome(s[1:len(s)-1])
    
s=input("Enter a string: ")
print(is_palindrome(s))