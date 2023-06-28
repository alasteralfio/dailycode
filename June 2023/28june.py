# CodeWars
# 28/6/2023

# https://www.tiktok.com/t/ZT8e8FB2G/ this game

import random

def display_game_board(game_board):
    print("Current Positions:")
    for position, number in enumerate(game_board):
        if number is None:
            number = 0
        print(f"{position + 1}. {number}")

def play_game():
    game_board = [None] * 20

    for i in range(20):
        rolled_number = random.randint(1, 999)
        position = -1

        while position < 0 or position >= 20 or game_board[position] is not None:
            user_input = input(f"Roll {i+1}: {rolled_number}. Choose a position (1-20) or enter 'A' to view all: ")
            if user_input.upper() == 'A':
                display_game_board(game_board)
                continue
            position = int(user_input) - 1

        game_board[position] = rolled_number

        if position > 0 and game_board[position-1] is not None and game_board[position-1] > game_board[position]:
            print("Game over.")
            return

        if i > 0 and game_board[i-1] is not None and game_board[i-1] > rolled_number:
            print("Game over.")
            return

    if sorted(game_board) == game_board:
        print("Congratulations! You win.")
    else:
        print("Sorry, you lose.")

play_game()
