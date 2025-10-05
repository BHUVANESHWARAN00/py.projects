
import random  
player_wins = 0
computer_wins = 0
ties = 0

while True:

    player = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    
    if player not in ['r', 'p', 's']:
        print("invalid choice. Please type r, p, or s.")
        continue 
    computer = random.choice(['r', 'p', 's'])
    
    print("Computer chose:", computer)
    
    if player == computer:
        print("It's a tie!")
        ties += 1
    elif (player == 'r' and computer == 's') or \
         (player == 'p' and computer == 'r') or \
         (player == 's' and computer == 'p'):
        print("You won this round!")
        player_wins += 1
    else:
        print("You lost this round!")
        computer_wins += 1
    
    print(f"Score so far -> You: {player_wins}, Computer: {computer_wins}, Ties: {ties}")

    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("\nFinal Score:")
        print(f"You won: {player_wins} times")
        print(f"Computer won: {computer_wins} times")
        print(f"Ties: {ties}")
        print("Thanks for playing!")
        break
