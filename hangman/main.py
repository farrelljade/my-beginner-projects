import random
from word_list import wrd_list

"""
Play a game of Hangman.
    
Randomly selects a word from 'wrd_list' and prompts the user to guess letters.
The user has 10 guesses to uncover the hidden word by guessing its letters.
Displays the progress after each guess and ends when the word is guessed or guesses run out.
"""

rndm_word = random.choice(wrd_list)
display = ["_" for l in rndm_word]
print(' '.join(display))

guesses = 10

while True:
    user_choice = input("\nGuess a letter: ")
    if user_choice not in rndm_word or user_choice in display:
        guesses -= 1
        print(f"Guesses remaining: {guesses}")
        if guesses == 0:
            print(f"Out of guesses!\nThe word was: '{rndm_word}'")
            break 

    for i in range(len(rndm_word)):
        if rndm_word[i] == user_choice:
            display[i] = user_choice


    print(' '.join(display))
    if "_" not in display:
        print(f"You guessed the word: '{rndm_word}'")
        break