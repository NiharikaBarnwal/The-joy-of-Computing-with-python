def fizzbuzz(r):
    for i in range(101,r):
        if i%3==0 and i%5==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"buzz")
        elif i%3==0:
            print(i,"fizzbuzz")
        else:
            print(i)

fizzbuzz(121)