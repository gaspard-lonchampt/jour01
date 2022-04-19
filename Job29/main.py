import math 

def Skywalker():
    list = []
    x = 0
    while x < 1:
        try:
            i = int(input("enter a grade "))
            if i > 40:
                if i%10 > 5 and i%5 >= 2:
                    print("ici modul 10")
                    i = math.ceil(i/5)*5
                    list.append(i)
                elif i%5 >= 3:
                    print("ici modul 3")
                    i = math.ceil(i/5)*5
                    list.append(i)
                else: 
                    print("ici else")
                    list.append(i)
            x += 1
        except:
            x = x
            print("I said a number, not a float or a string, A NUMBER !")
    
    print(list)

Skywalker()
