class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount


def main():
    # Create lunch cards for Peter and Grace
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)

    # Peter eats a luxury lunch
    peter_card.eat_luxury()

    # Grace eats an ordinary lunch
    grace_card.eat_ordinary()

    # Print balances
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    # Peter deposits 20 euros
    peter_card.deposit_money(20)

    # Grace eats a luxury lunch
    grace_card.eat_luxury()

    # Print balances again
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    # Peter eats an ordinary lunch twice
    peter_card.eat_ordinary()
    peter_card.eat_ordinary()

    # Grace deposits 50 euros
    grace_card.deposit_money(50)

    # Print final balances
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")


if __name__ == "__main__":
    main()
