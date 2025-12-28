import random
def generate_secret():
    digits = []
    while len(digits) < 4:
        num = random.randint(0, 9)
        if num not in digits:
            digits.append(num)
    return digits

def get_cows_bulls(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return cows, bulls


secret_number = generate_secret()

print("Try to guess the 4-digit number. All digits are unique.")

while True:
    user_input = input("Enter your guess: ")
    if len(user_input) != 4 or not user_input.isdigit():
        print("Guess must be 4 digits.")
        continue
    
    guess = [int(d) for d in user_input]

    if len(set(guess)) != 4:
        print("All digits must be different.")
        continue
    cows, bulls = get_cows_bulls(secret_number, guess)
    print(cows, "cow(s),", bulls, "bull(s)")
    if bulls == 4:
        print("Congratulations! You guessed the number:", ''.join(map(str, secret_number)))
    break
