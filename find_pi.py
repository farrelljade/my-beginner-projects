from math import pi

pi = pi  # PI built into the math module already

user = int(input("\nHow many decimal places do you want PI printed to: "))

decimal_place = user
answer = round(pi, user)  # use the round() function to round to a decimal place. 

print(f"PI to {decimal_place} decimal places is: {answer}")