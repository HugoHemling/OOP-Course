import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    while user_wins < 3 and computer_wins < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_wins += 1
            print("You win this round!")
        elif winner == "computer":
            computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        print(f"Score - You: {user_wins}, Computer: {computer_wins}")
    if user_wins == 3:
        print("Congratulations! You won the game!")
    else:
        print("Sorry! The computer won the game!")

if __name__ == "__main__":
    play_game()
    