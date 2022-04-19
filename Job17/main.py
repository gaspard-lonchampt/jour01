def numberList():
    list = []
    x = 1
    for x in range (1, 101):
        if x%5 != 0 and x%3 != 0:
            list.append(x)
        else:    
            if x%5 == 0 and x%3 == 0:
                i = "FizzBuzz"
            if x%5 == 0:
                i = "Buzz"
            else:
                i = "Fizz"
            list.append(i)
    
    print(list)

numberList()