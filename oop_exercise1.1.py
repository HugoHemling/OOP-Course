def count_integer_type():
    neg_count = 0
    even_count = 0 

    while True:
        num = int(input("Enter an integer: "))
        if num < 0:
            neg_count += 1
        if num % 2 == 0:
            even_count += 1
        if num == 0:
            break

    print("Number of negative integers: ", neg_count)
    print("Number of even integers: ", even_count)


count_integer_type()


