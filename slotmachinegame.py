import random
 
class SlotMachine:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
 
    def spin_reels(self):
        return [random.choice(self.symbols) for _ in range(3)]
 
    def calculate_payout(self, reels, bet):
        if reels[0] == reels[1] == reels[2]:
            return bet * 10   # Three symbols match
        elif len(set(reels)) == 2:
            return bet * 2    # Two symbols match
        else:
            return -bet       # No match
 
    def play_round(self, bet):
        if bet > self.balance:
            print("You cannot bet more than your balance!")
            return
        
        reels = self.spin_reels()
        print(" | ".join(reels))
        
        payout = self.calculate_payout(reels, bet)
        self.balance += payout
        
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print(f"You lost ${-payout}.")
 
    def can_play(self):
        return self.balance > 0
 
 
def main():
    balance = float(input("Enter your starting balance: $"))
    game = SlotMachine(balance)
 
    while game.can_play():
        print(f"\nCurrent balance: ${game.balance:.2f}")
        bet = float(input("Enter your bet amount: $"))
        game.play_round(bet)
        
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break
 
    print(f"\nGame over! Your final balance is ${game.balance:.2f}")
 
main()
 