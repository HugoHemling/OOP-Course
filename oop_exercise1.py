import random

number_list = []
string_list = []

print("Enter 10 numbers: ")
for i in range(10):
    number = int(input("Enter number: "))
    number_list.append(number)

print("Enter 10 strings: ")
for i in range(10):
    string = input("Enter string: ")
    string_list.append(string)

print("Number List: ", number_list)
print("String List: ", string_list)

number_list = [random.randint(1, 100) for i in range(10)]

print("Randomly generated number list: ", number_list)
