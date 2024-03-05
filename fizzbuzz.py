#final branch
i = 1 #start with number 1

while(i <= 100):
    #check if i is a multiple of 3 and 5 first
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    #check if i is a multiple of 3
    elif(i % 3 == 0):
        print("Fizz")
    #check if i is a multiple of 5
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)
    #after checking all conditions increment by 1
    i += 1 