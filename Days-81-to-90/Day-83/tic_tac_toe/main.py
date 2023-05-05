from variables import Banner, board, positions


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def take_turn(player):
    print("\n")
    print(f"{player}'s turn")
    position = input("Choose a position [1-9]: ")
    while position not in positions:
        position = input("Invalid input.\nChoose a position [1-9]: ")
    while position == "help":
        print_help()
        print("------------------------------------------------------------------\n")
        print_board()
        position = input("Choose a position [1-9]: ")
    else:
        position = int(position) - 1
        while board[position] != "-":
            position = int(input("Position already taken.\nChoose a position [1-9]: "))
        board[position] = player
        print("\n")
        print_board()


def check_game_over():
    if (board[0] == board[1] == board[2] != "-") or \
            (board[3] == board[4] == board[5] != "-") or \
            (board[6] == board[7] == board[8] != "-") or \
            (board[0] == board[3] == board[6] != "-") or \
            (board[1] == board[4] == board[7] != "-") or \
            (board[2] == board[5] == board[8] != "-") or \
            (board[0] == board[4] == board[8] != "-") or \
            (board[2] == board[4] == board[6] != "-"):
        return "win"

    elif "-" not in board:
        return "tie"

    else:
        return "play"


def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(f"{current_player} wins!")
            game_over = True
        elif game_result == "tie":
            print(f"It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


def print_help():
    print(
        '''
Instructions: 
1. The game is to be played between two people.
2. One of the player chooses ‘X’ and the other ‘O’ to mark their respective cells.
3. The game starts with one of the players and the game ends when one of the players has one whole row/ column/ diagonal 
   filled with his/her respective character (‘X’ or ‘O’).

Board Layout:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
        '''
    )


print(Banner)
play_game()
