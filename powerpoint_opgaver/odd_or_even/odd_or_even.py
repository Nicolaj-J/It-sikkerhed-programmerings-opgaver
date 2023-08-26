try:
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        print("You entered an even number")
    else:
        print("You entered an odd number")
except ValueError:
    print("Enter an integer please")