import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def get_computer_move(board):
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    for _ in range(9):
        print_board(board)
        
        if _ % 2 == 0:
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
            if board[row][col] != " ":
                print("Invalid Move!")
                continue
            board[row][col] = player
        else:
            row, col = get_computer_move(board)
            print(f"Computer chooses {row}, {col}")
            board[row][col] = computer

        if check_win(board, player):
            print_board(board)
            print("You win!")
            return
        elif check_win(board, computer):
            print_board(board)
            print("Computer wins!")
            return

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
