while True:
    i = int(input("Enter a number you want to check whether it is prime: "))

    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                print(i, "is not a prime number")
                break
        else:
            print(i, "is a prime number")
    else:
        print(i, "is not a prime number")

# because it takes a long time to check one by one