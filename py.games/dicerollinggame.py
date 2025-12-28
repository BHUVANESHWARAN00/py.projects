import random

num_dice = int(input("How many dice do you want to roll? "))

if num_dice == 0:
    print("You can't play.")
else:
    roll_count = 0
    while True:
        results = []
        for i in range(num_dice):
            results.append(random.randint(1, 6))
        print(tuple(results))
        
        roll_count += 1
        
        answer = input("Roll the dice? (y/n): ").lower()
        
        if answer == 'y':
            continue
        elif answer == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input.")
            break
    print("Total rolls:",roll_count)
