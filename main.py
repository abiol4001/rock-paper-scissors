import random

while True:
    # User making a choice
    user_action = input("Enter a choice (rock, paper, scissors): ")
    user_action = user_action.lower()

    # List of Choices
    possible_actions = ["rock", "paper", "scissors"]
    # Computer's choice
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action} computer chose {computer_action}.\n")

    # Determine a Winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}, it's a tie!")
    elif user_action == "rock":
        if computer_action  == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


