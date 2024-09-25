myString = input("Enter a string :")
def vowel(myString):
  lst=[]
  sum=0
  for i in myString:
      if(i.lower() in ['a','e','i','o','u']):
          if i not in lst:
              lst.append(i)
              sum+=myString.count(i)
  return sum
print("The no. of vowels is : ",vowel(myString))