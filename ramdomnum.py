import random

min_number = int(input("Minimum number: "))
max_number = int(input("Maximum number: "))

secret_number = random.randint(min_number, max_number)

max_tries = int(input("How many guesses do you want? "))
tries = 0

while tries < max_tries:
    guess = int(input(f"Guess a number between {min_number} and {max_number}: "))
    tries += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {tries} tries!")
        break

if guess != secret_number:
    print(f"Out of guesses! The number was {secret_number}.")