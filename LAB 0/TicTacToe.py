def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    
    for row in board:
        if all(cell == player for cell in row):
            return True

    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
  
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != "_" for row in board for cell in row)

def tic_tac_toe():
    board = [["_"] * 3 for _ in range(3)]
    current_player = "X"

    print("Tic Tac Toe: Player vs Player")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn:")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "_":
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")

tic_tac_toe()
