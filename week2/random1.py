import random
with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("\nI am fine.")
myfile.close
# Four modes are there :
# 1. r - read the file
# 2. w - write the file (the already existing file will be removed)
# 3. a - append the file (add new data to the existing file)
# 4. r+ - both read and write operations can be done

random.randint(1,5) #includes 1 and 5
random.randrange(1,5) #excludes 5
random.random #generates random real number from 0 to 1
random.randrange(1,10,2) #excludes 10 and generates only odd numbers(the second number after the current number)
random.choice([1,4,2,0,9]) # generates random number from the list
