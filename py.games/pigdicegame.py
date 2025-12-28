import random

player_scores = [0, 0]
current_player = 0
WINNING_SCORE = 100
print("First player to reach 100 points wins!\n")

while True:
    print(f"\n--- Player {current_player + 1}'s turn ---")
    turn_total = 0  
    while True:
        print(f"Current total score: {player_scores[current_player]}")
        print(f"Turn total: {turn_total}")

        choice = input("Do you want to 'r' (roll) or 'h' (hold)? ").lower()

        if choice == 'r':
            roll = random.randint(1, 6)
            print(f"You rolled a {roll} ")

            if roll == 1:
                print("Oh no! You rolled a 1 You lose all turn points!")
                turn_total = 0
                break 
            else:
                turn_total += roll

        elif choice == 'h':
            player_scores[current_player] += turn_total
            print(f"You held. Your total score is now {player_scores[current_player]}.")
            break  
        else:
            print("Invalid choice. Please enter 'r' or 'h'.")

    if player_scores[current_player] >= WINNING_SCORE:
        print(f"\n Player {current_player + 1} wins with {player_scores[current_player]} points! 🏆")
        break

    current_player = 1 -current_player
