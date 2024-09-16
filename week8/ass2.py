def are_anagrams(str1, str2):
    str1_fil = ''.join(char for char in str1.lower() if char.isalpha())
    str2_fil = ''.join(char for char in str2.lower() if char.isalpha())
    if sorted(str1_fil) == sorted(str2_fil):
        return 1
    else:
        return 0
str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")

print(are_anagrams(str1, str2))
