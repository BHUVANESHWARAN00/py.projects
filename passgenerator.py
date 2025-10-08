import random

length = int(input("Enter the length of your password: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*()-_+=<>?/"

characters = lowercase_letters
if use_upper:
    characters += uppercase_letters
if use_numbers:
    characters += numbers
if use_special:
    characters += special_chars

password = ""
for i in range(length):
    password += random.choice(characters)

print(f"Your generated password is:{password}")
