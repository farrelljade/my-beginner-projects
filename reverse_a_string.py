# User to enter a sentence. The sentence should then be reversed and printed out.

user = input("Please enter a sentence:\n\n")

# Here we slice the string. [::-1] results in the string being reversed from the last character.
reversed_string = user[::-1]

print(reversed_string)