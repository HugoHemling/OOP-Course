import random

number_list = []
string_list = []

print("Enter 10 numbers: ")
for i in range(10):
    number = int(input("Enter number: "))
    number_list.append(number)

print("\nEnter 10 strings: ")
for i in range(10):
    string = input("Enter string: ")
    string_list.append(string)

print("\nNumber List: ", number_list)
print("\nString List: ", string_list)

number_list = [random.randint(1, 100) for i in range(10)]

print("\nRandomly generated number list: ", number_list)

number_list.sort()
string_list.sort()

print("\nSorted numbers: ",number_list)
print("Sorted string list: ",string_list)
