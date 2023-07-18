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
computer_row, computer_col = random.randint(0, 4), random.randint(0, 4)
# player_row, player_col = random.randint(0, 4), random.randint(0, 4)


# while (computer_row == player_row and computer_col == player_col):
#     computer_row, computer_col = random.randint(0, 2), random.randint(0, 2)

while True:
    # print(f"your tic is room:{player_row,player_col}")
    movement = input("Enter your choice move in board? ")
    new_player_row, new_player_col = player_row, player_col
    # movement = movement.lower()
    player_row=movement[0]
    # print(player_row)
    player_col=movement[1]
    # print(player_col)
    box[player_row][player_col] = 'X'
    player_row, player_col = new_player_row, new_player_col
    box[player_row][player_col] = 'X'

    if (computer_row == player_row and computer_col == player_col):
        computer_row, computer_col = random.randint(0, 2), random.randint(0, 2)
