def main():
    phone_book = {}

    while True:
        command = input("Command (1 search, 2 add, 3 quit): ")
        if command == "1":
            name = input("Enter name: ")
            if name in phone_book:
                print(f"Phone number: {phone_book[name]}")
            else:
                print("no number.")
        elif command == "2":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            phone_book[name] = phone_number
            print("ok!")
        elif command == "3":
            print("quitting...")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()