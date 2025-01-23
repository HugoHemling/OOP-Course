def count_integer_type():
    neg_count = 0
    even_count = 0 
    sum_pos_divby3 = []

    while True:
        num = int(input("Enter an integer: "))
        if num < 0:
            neg_count += 1
        if num % 2 == 0:
            even_count += 1
        if num > 0 and num % 3 == 0:
            sum_pos_divby3.append(num)
        if num == 0:
            break

    print("Number of negative integers: ", neg_count)
    print("Number of even integers: ", even_count)
    print("Number of positive integers divisible by 3: ", sum(sum_pos_divby3))



count_integer_type()


