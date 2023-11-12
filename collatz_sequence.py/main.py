"""
Collatz Sequence

This script takes an integer input from the user and applies the Collatz sequence
algorithm until the number reaches 1. The Collatz sequence operates as follows:
- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.

The program will continue to display the resulting numbers until reaching 1.
"""

def collatz(number):  
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1
        print(number)

while True:
    try:
        user_choice = int(input("\nChoose a number: "))
        collatz(user_choice)
        break
    except ValueError:
        print("Must be an integer number.")