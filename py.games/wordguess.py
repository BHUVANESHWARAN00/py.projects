import random
 
def word_guess_game():
    words = ["apple", "banana", "orange", "grape", "mango", "pizza", "computer"]
    secret = random.choice(words)
    guessed = []
    hint_used = False
 
    print("Welcome to Word Guess!")
    print(f"The word has {len(secret)} letters.")
 
    # Player chooses number of attempts
    while True:
        try:
            attempts = int(input("How many attempts would you like? "))
            if attempts > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Enter a valid number, please!")
 
    # Main game loop
    while attempts > 0:
        display = "".join([ch if ch in guessed else "_" for ch in secret])
        print("Word:", display)
 
        guess = input("Enter a letter or 'hint': ").lower()
 
        # Hint feature
        if guess == "hint":
            if not hint_used:
                for ch in secret:
                    if ch not in guessed:
                        guessed.append(ch)
                        print(f"Hint: The letter '{ch}' is in the word.")
                        hint_used = True
                        break
            else:
                print("You've already used your hint!")
            continue
 
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue
 
        if guess in guessed:
            print("You already guessed that letter.")
            continue
 
        if guess in secret:
            guessed.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
 
        # Win check
        if all(ch in guessed for ch in secret):
            print(f"Congratulations! You guessed the word: '{secret}'.")
            return
 
    print(f"Out of attempts! The word was '{secret}'.")
 
if __name__ == "__main__":
    word_guess_game()
 