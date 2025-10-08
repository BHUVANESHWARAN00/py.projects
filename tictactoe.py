from colorama import Fore, Style, init
init(autoreset=True)

def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    print("\nCurrent Board:")
    for row in board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + cell, end=" | ")
            elif cell == "O":
                print(Fore.BLUE + cell, end=" | ")
            else:
                print(cell, end=" | ")
        print("\n" + "-" * (size * 4))

def check_winner(board, player):
    size = len(board)

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True

    if all(board[i][i] == player for i in range(size)) or all(board[i][size-1-i] == player for i in range(size)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():

    while True:
        try:
            size = int(input("Enter board size (3-5): "))
            if size not in [3, 4, 5]:
                print("Please choose 3, 4, or 5.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    board = create_board(size)
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter column (0-{size-1}): "))
        except ValueError:
            print("Enter valid numbers!")
            continue

        if row not in range(size) or col not in range(size):
            print("Invalid input!")
            continue

        if board[row][col] != " ":
            print("Cell already taken!")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(Fore.GREEN + f"Player {current_player} wins!")
            return current_player

        if check_draw(board):
            print_board(board)
            print(Fore.YELLOW + "It's a draw!")
            return "Draw"

        current_player = "O" if current_player == "X" else "X"

def tic_tac_toe():
    scores = {"X": 0, "O": 0, "Draw": 0}

    while True:
        winner = play_game()
        if winner in ["X", "O"]:
            scores[winner] += 1
        else:
            scores["Draw"] += 1

        print("\nScoreboard:")
        print(Fore.RED + f"Player X: {scores['X']}")
        print(Fore.BLUE + f"Player O: {scores['O']}")
        print(Fore.YELLOW + f"Draws: {scores['Draw']}")

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

tic_tac_toe()
