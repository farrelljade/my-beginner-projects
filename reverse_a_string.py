# User to enter a sentence. The sentence should then be reversed and printed out.

user = input("\nEnter your message:\n")

# Here we slice the string. [::-1] results in the string being reversed from the last character.
reversed_string = user[::-1]

print(f"\nYour message reversed is:\n{reversed_string}")