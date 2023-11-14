import random

"""
Higher-Lower Number Guessing Game

This Python program implements a simple Higher-Lower number guessing game. The computer randomly selects
a number between 1 and 100, and the player has to guess the correct number. After each guess, the program
provides feedback whether the player should guess higher or lower. The game continues until the player
correctly guesses the number.

The player can choose to play again after finishing a round.

Usage:
1. Run the program, and it will prompt you to guess a number between 1 and 100.
2. After each guess, the program will indicate whether you should guess higher or lower.
3. Once you correctly guess the number, the program will display the number of guesses it took.
4. You can choose to play again by entering 'yes' or 'y' when prompted.
"""

def higherLower():
    keep_guessing = True
    guesses = 0

    comp_choice = random.randint(1, 100)
    user_choice = int(input("Select a number between 1 - 100: "))

    while keep_guessing:
        guesses += 1
        if user_choice == comp_choice:
            print("\nCongratulations! You guessed the computers number.")
            print(f"It took you {guesses} guesses.")
            play_again = input("Play again? ").lower()
            if play_again in ["yes", "y"]:
                higherLower()
            elif play_again in ["no", "n", ""]:
                break
        elif user_choice < comp_choice:
            print("Guess higher")
        elif user_choice > comp_choice:
            print("Guess lower")

        user_choice = int(input("Guess again: "))

higherLower()