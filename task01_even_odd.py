while True:
    number = int(input("Enter a number: "))

    if number == 0:
        print("Zero.\n")
    elif number % 2 == 0:
        print("The number is even.\n")
    else:
        print("The number is odd.\n")