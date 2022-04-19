def numberList():
    list = []
    x = 0
    while x < 5:
        try:
            i = int(input("enter a number "))
            list.append(i)
            x += 1
        except:
            x = x
            print("I said a number, not a float or a string, A NUMBER !")
    
    list.sort()
    print(list)

numberList()