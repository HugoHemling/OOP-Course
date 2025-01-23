import random


def roll_die():
    return random.randint(1, 6)


result = roll_die()
print(result)