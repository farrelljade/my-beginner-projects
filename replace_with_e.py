# Define a function to replace characters with 'e' until a period is encountered
def replace_with_e(input_string):
    result = ""  # Create an empty string to build the output
    replace = True  # To control replacement

    # Iterate through each character in the input string
    for char in input_string:
        if replace and char != ".":  # If the flag is True and the character is not a period
            result += "e"  # Replace with 'e'
        else:
            result += char  # Keep the character as is
            replace = False  # Set the flag to False after the first period

    return result  # Return the modified string

# Get user input a number
user_input = input("Type a number. The number will be converted to 'e' upto the decimal place: ")

# Call the function and store the result in the output_string
output_string = replace_with_e(user_input)

# Display the modified string
print("Replaced with 'e' until period: ", output_string)