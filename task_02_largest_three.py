while True:
    x = int(input("Enter a first number: "))
    y = int(input("Enter a second number: "))
    z = int(input("Enter a third number: "))

    if x >= y and x >= z:
        print("The largest number is:", x)
    elif y >= x and y >= z:
        print("The largest number is:", y)
    else:  
        print("The largest number is:", z)