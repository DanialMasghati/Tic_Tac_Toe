import os
import random


def create_board(rows=3, cols=3):
    """Create an empty game board."""
    return [["-" for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    """Print the game board."""
    for row in board:
        print(" ".join(row))


def get_player_move(player, board):
    """Get the move from the specified player."""
    while True:
        movement = input(f"Enter your move (player {player}): ")
        try:
            row, col = map(int, movement.strip().split())
            if check_move(row, col, board):
                if board[row][col] == "-":
                    return row, col
                else:
                    print("Invalid move, cell already occupied.")
            else:
                print("Invalid move, please try again.")
        except ValueError:
            print("Invalid input, please enter two integers separated by a space.") # noqa E501


def get_computer_move(board):
    """Get the move from the computer player."""
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == "-":
            return row, col


def check_move(player_row, player_col, board):
    """Check if a move is valid."""
    return 0 <= player_row < len(board) and 0 <= player_col < len(board[0])


def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    # No winner
    return None


def play_game():
    """Play a game of Tic Tac Toe."""

    # Create an empty game board
    board = create_board()

    # Define the players
    human_player = "X"
    computer_player = "O"

    # Set the first player randomly
    players = [human_player, computer_player]
    current_player = random.choice(players)

    # Play the game
    while True:
        clear_screen()
        # Print the current state of the game board
        print_board(board)

        # Get the move from the current player
        if current_player == human_player:
            # Human player's move
            move = get_player_move(human_player, board)
        else:
            # Computer player's move
            move = get_computer_move(board)

        # Check if the player wants to quit
        if move is None:
            print("Game has been quit.")
            break

        # Update the game board with the player's move
        row, col = move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break

        # If the board is full and there is no winner, print a tie and break the loop # noqa E501
        if all(all(cell != "-" for cell in row) for row in board):
            print_board(board)
            print("Tie!")
            break

        # Switch to the other player
        current_player = human_player if current_player == computer_player else computer_player # noqa E501


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
