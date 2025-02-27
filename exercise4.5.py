class LunchCard:
    def __init__(self, balance: float):
        """Initialize the LunchCard with a given balance."""
        self.balance = balance

    def __str__(self):
        """Return a formatted string of the balance."""
        return f"The balance is {self.balance:.1f} euros"

    def subtract_from_balance(self, amount: float) -> bool:
        """Subtract the given amount from the balance if sufficient funds exist.
        Returns True if successful, False otherwise."""
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit_money(self, amount: float):
        """Deposit money onto the card. Raises an error if the amount is negative."""
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount


class PaymentTerminal:
    def __init__(self):
        """Initialize the payment terminal with default funds and lunch prices."""
        self.funds = 1000.0  # Initial funds in the terminal
        self.regular_lunch_price = 2.95
        self.special_lunch_price = 5.90
        self.regular_lunches_sold = 0
        self.special_lunches_sold = 0

    def pay_with_cash(self, amount_paid: float, lunch_type: str) -> float:
        """Handles cash payments for lunch. Returns the change if successful, otherwise returns the full amount paid."""
        if lunch_type == "regular" and amount_paid >= self.regular_lunch_price:
            self.funds += self.regular_lunch_price
            self.regular_lunches_sold += 1
            return amount_paid - self.regular_lunch_price  # Change returned
        elif lunch_type == "special" and amount_paid >= self.special_lunch_price:
            self.funds += self.special_lunch_price
            self.special_lunches_sold += 1
            return amount_paid - self.special_lunch_price  # Change returned
        return amount_paid  # Not enough money, full amount returned

    def pay_with_card(self, card: LunchCard, lunch_type: str) -> bool:
        """Handles LunchCard transactions for lunch payments. 
        Returns True if payment is successful, False otherwise."""
        if lunch_type == "regular" and card.subtract_from_balance(self.regular_lunch_price):
            self.regular_lunches_sold += 1
            return True
        elif lunch_type == "special" and card.subtract_from_balance(self.special_lunch_price):
            self.special_lunches_sold += 1
            return True
        return False  # Payment failed

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        """Deposits money onto the LunchCard and adds the same amount to the terminal funds."""
        if amount > 0:
            card.deposit_money(amount)
            self.funds += amount

    def get_funds(self) -> float:
        """Returns the available funds at the terminal."""
        return self.funds

    def get_sales_report(self):
        """Prints the number of lunches sold and the available funds."""
        print(f"Funds available at the terminal: {self.funds:.2f}")
        print(f"Regular lunches sold: {self.regular_lunches_sold}")
        print(f"Special lunches sold: {self.special_lunches_sold}")


# Example usage:
if __name__ == "__main__":
    terminal = PaymentTerminal()
    card = LunchCard(2)

    print(f"Card balance is {card.balance:.1f} euros")

    success = terminal.pay_with_card(card, "special")
    print("Payment successful:", success)  # Expected Output: False
    print(f"Card balance is {card.balance:.1f} euros")

    terminal.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance:.1f} euros")

    success = terminal.pay_with_card(card, "special")
    print("Payment successful:", success)  # Expected Output: True
    print(f"Card balance is {card.balance:.1f} euros")

    terminal.get_sales_report()
