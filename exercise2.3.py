
import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.choices(
            ['Heads', 'Tails', 'Upright', 'Rabbit Hole', 'Wormhole'],
            weights=[45, 45, 5, 4, 1],
            k=1
        )[0]
        self.sideup = outcome

    def get_sideup(self):
        return self.sideup

# Main function definition

def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

# Calling the main function
main()