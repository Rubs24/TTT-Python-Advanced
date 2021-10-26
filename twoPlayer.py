from common import *

board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]

def handle_turn(player):
    print(player + "'s turn ")
    position = input("Choose a number between 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input ("invalid please select a number 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there go again: ")
            
    board[position] = player
    display_board(board)

def two_player_game():
    global current_player
    global game_ongoing
    global board
    display_board(board)
    current_player = "X"
    game_ongoing = True
    while game_ongoing:
        handle_turn(current_player)
        game_ongoing = check_game_over(board)
        current_player = flip_player(current_player)
    end_reset()
    current_player = "X"
    board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]