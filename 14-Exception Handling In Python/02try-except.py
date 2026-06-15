while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        c = a/b
        print(c)
    except ZeroDivisionError :
        print("Hey! don't divide by zero")
    except ValueError :
        print("Please don't type bad typecasts.")
    