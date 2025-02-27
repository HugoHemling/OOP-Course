class NumberStats:
    def __init__(self):
        # Initialize count and sum
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        # Increment count and add to total sum
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self):
        # Return the count of numbers added
        return self.numbers

    def get_sum(self):
        # Return the sum of numbers added
        return self.total_sum

    def average(self):
        # Return the mean, return 0 if no numbers have been added
        return self.total_sum / self.numbers if self.numbers > 0 else 0


def main():
    all_numbers = NumberStats()  # Tracks all numbers
    even_numbers = NumberStats()  # Tracks even numbers
    odd_numbers = NumberStats()  # Tracks odd numbers

    print("Please type in integer numbers:")

    while True:
        number = int(input())  # Get user input
        if number == -1:  # Stop when -1 is entered
            break
        
        all_numbers.add_number(number)  # Add to all numbers
        
        if number % 2 == 0:
            even_numbers.add_number(number)  # Add to even numbers
        else:
            odd_numbers.add_number(number)  # Add to odd numbers

    print("Sum of numbers:", all_numbers.get_sum())
    print("Mean of numbers:", all_numbers.average())
    print("Sum of even numbers:", even_numbers.get_sum())
    print("Sum of odd numbers:", odd_numbers.get_sum())


if __name__ == "__main__":
    main()
