while True:
    try:
        number = int(input("Write a number: "))+1
        for i in range(1,number):
            ls = []
            for n in range(1,number):   
                ls.append("{:4}".format(str(i*n)))
            print(*ls)
        break
    except ValueError:
        print("Make sure you input an integer")