import random

# Rock Paper Scissors
R = "rock"
P = "paper"
S = "scissors"

user_win = 0
comp_win = 0

while True:  # Start an outer loop for the entire game
    
    x = input("rock, paper, scissors? (Type 'quit' to exit): ").lower()
    if x == 'quit':
        break  # Exit the game loop if the user wants to quit
    
    choice = random.choice([R, P, S])
    print(f"Computer chose: {choice}")
    
    if choice == x:
        print("It was a draw")
    elif x == R:
        if choice == S:
            print("You win")
            user_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
        else:
            print("You lose")
            comp_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
    elif x == P:
        if choice == R:
            print("You win")
            user_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
        else:
            print("You lose")
            comp_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
    elif x == S:
        if choice == P:
            print("You win")
            user_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
        else:
            print("You lose")
            comp_win += 1
            print("Your score is: ", str(user_win))
            print("Computer score is: ", str(comp_win))
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break  # Exit the game loop if the user doesn't want to play again


# TIC TAC TOE GAME
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_move():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for _ in range(9):
        player = players[current_player]
        print(f"Player {player}'s turn.")
        row, col = get_move()

        while board[row][col] != " ":
            print("Cell already taken. Try again.")
            row, col = get_move()

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            return

        if is_board_full(board):
            print("It's a tie!")
            return

        current_player = 1 - current_player

if __name__ == "__main__":
    play_tic_tac_toe()

#calculator

def add(a, b):
    answer = a + b
    print(a, b )

def sub(a, b):
    answer = a - b
    print(a, b )

def mul(a, b):
    answer = a * b
    print(a, b )

def div(a, b):
    answer = a / b
    print(a, b )

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your operation: ")
    
    if choice == "a" or choice == "A":
       print("Addition")
       a = int(input("Input first number: "))
       b = int(input("Input second number"))
       add(a, b)

    elif choice == "b" or choice == "B":
       print("Subtraction")
       a = int(input("Input first number: "))
       b = int(input("Input second number"))
       sub(a, b)
    
    elif choice == "c" or choice == "C":
       print("Multiplication")
       a = int(input("Input first number: "))
       b = int(input("Input second number"))
       mul(a, b)

    elif choice == "d" or choice == "D":
       print("Division")
       a = int(input("Input first number: "))
       b = int(input("Input second number"))
       div(a, b)

    elif choice == "e" or choice == "E":
       print("program ended")
       quit()

import random

def watch():
    x = input("Do you want to play again (yes/no): ")
    if x.lower() != "yes":
        quit()

while True:
    user_guess = input("Guess the number between 1 to 20: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 20:
            print("Guess a number between 1 and 20")
        else:
            computer_guess = random.randint(1, 20)
            print("The computer guessed:", computer_guess)

            if user_guess != computer_guess:
                print("You lost")
            else:
                print("You won")

        watch()
    else:
        print("Please type a number next time")