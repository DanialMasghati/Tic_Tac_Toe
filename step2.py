import os
import random

# Define the size of the box
rows = 3
cols = 3

# Create an empty list to store the box
box = []

# Loop through each row
for i in range(rows):
    # Create a list to represent a row
    row = []
    # Loop through each column
    for j in range(cols):
        # Append "1" to the row list for each cell
        row.append("-")
    # Append the row list to the box list
    box.append(row)

# print(box)
for row in box:
    print(" ".join(row))

EXIT_COMMAND = ("quit", "q", "ex", "exit")

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')

def check_move(player_row, player_col):
    return 0 <= player_row < 3 and 0 <= player_col < 3

# Define the players
human_player = "X"
computer_player = "O"

# Set the first player randomly
players = [human_player, computer_player]
current_player = random.choice(players)

# Loop until there is a winner or the board is full
while True:
    # Print the current state of the game board
    for row in box:
        print(" ".join(row))

    # Get the move from the current player
    if current_player == human_player:
        # Human player's move
        while True:
            movement = input("Enter your choice move in board? ")
            try:
                row, col = map(int, movement.strip())
                if check_move(row, col) and box[row][col] == "-":
                    box[row][col] = human_player
                    break
                else:
                    print("Invalid move, please try again.")
            except ValueError:
                print("Invalid input, please enter two integers separated by a space.")

    else:
        # Computer player's move
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if box[row][col] == "-":
                box[row][col] = computer_player
                break

    # Check for a winner
    winner = None

    # Check rows
    for row in box:
        if row[0] == row[1] == row[2] != "-":
            winner = row[0]
            break

    # Check columns
    if not winner:
        for i in range(3):
            if box[0][i] == box[1][i] == box[2][i] != "-":
                winner = box[0][i]
                break

    # Check diagonals
    if not winner:
        if box[0][0] == box[1][1] == box[2][2] != "-":
            winner = box[0][0]
        elif box[0][2] == box[1][1] == box[2][0] != "-":
            winner = box[0][2]

    # If there is a winner, print the winner and break the loop
    if winner:
        print(f"{winner} wins!")
        break

    # If the board is full and there is no winner, print a tie and break the loop
    if all(all(cell != "-" for cell in row) for row in box):
        print("Tie!")
        break

    # Switch to the other player
    current_player = human_player if current_player == computer_player else computer_player
    clear_screen()