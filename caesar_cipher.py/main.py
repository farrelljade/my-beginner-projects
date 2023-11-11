"""
Caesar Cipher Project

This Python program implements a simple Caesar cipher encryption and decryption system.
Each letter in the plaintext is shifted can be shifted a certain number of places
up or down the alphabet.

Usage:
1. Choose whether to encrypt or decrypt a message.
2. Enter the message to be encrypted or decrypted.
3. Specify the shift amount for the Caesar cipher.
4. View the result.

Functions:
- encrypt_cipher(text, shift): Encrypts a given message using the Caesar cipher.
- decrypt_cipher(text, shift): Decrypts a given message using the Caesar cipher.

Options:
1. Encrypt message
2. Decrypt message
3. Quit
"""

def encrypt_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start - shift) % 26 +start)
        else:
            result += char
    return result

while True:
    enc_dec = input("\nDo you want to:\n1. Encrypt message\n2. Decrypt message\n3. Quit\n\n").lower()

    if enc_dec in ["1", "encrypt message", "encryptmessage"]:
        message = input("\nType message to encrypt: ")
        shift_amount = int(input("Shift amount: "))
        encoded_message = encrypt_cipher(message, shift_amount)
        print(f"Your encrypted message is: {encoded_message}")
    elif enc_dec in ["2", "decrypt message", "decryptmessage"]:
        message = input("Type your message to decrypt: ")
        shift_amount = int(input("Shift amount: "))
        decrypted_message = decrypt_cipher(message, shift_amount)
        print(f"Your decrypted message is: {decrypted_message}")
    elif enc_dec in ["3", "quit"]:
        break
    else:
        print("Invalid selection")
        break