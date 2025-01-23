def count_negative_integers():
    count = 0
    while True:
        num = int(input("Enter an integer: "))
        if num < 0:
            count += 1
        if num == 0:
            break

    print("Number of negative integers: ", count)


count_negative_integers()

