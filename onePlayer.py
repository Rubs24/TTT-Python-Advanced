import random
import time
from common import *;

x_1 = None
board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]
middle = False
cp = None

##### Handles Human Player Turns #####
def handle_turn(player):
    print( player + "'s turn ")
    global difficulty
    if player =="X":
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
    else:
        ai_move(difficulty)
    print()

##### Handles the move of the artificial intelligence based on the selected difficulty level #####
def ai_move(difficulty):
    time.sleep(0.25)
    print("thinking")
    time.sleep(0.75)
    if difficulty == 'e':
        position = easy_ai()
    elif difficulty=='m':
        position = med_ai()
    else:
        position = hard_ai()
    board[position] = "O"
    return

##### Easy AI selects cells at random #####
def easy_ai():
    valid = False
    while valid == False:
        pos = random.randrange(8)
        if board[pos] == "-":
            valid = True
            return pos

##### Medium AI selects cells at random if it's not a critcal move #####
def med_ai():
    global board
    if board.count("-") > len(board)-3:
       pos = easy_ai()
    else:
        ctw = close_to_win()
        b = block()
        if ctw!=None:
            pos = ctw
        elif b!=None:
            pos = b
        else:
            pos = easy_ai()
    return pos

##### Hard AI has every step determined and cannot be beaten, only tied #####
def hard_ai():
    global middle
    global board
    global last_move
    global x_1
    pos = 0
    if board.count("-") > len(board)-1:
        pos = 0
    elif board.count("-") > len(board)-3:
        if board[4] == "X":
                pos = 8
                middle = True
                x_1=4
        else:
            x_1 = board.index('X')
            if x_1  in [1,2,5,8]:
                pos=6
            else:
                pos=2
    elif board.count("-") > len(board)-5:
        cm = check_crit_move()
        if cm != None:
            pos = cm
        else:
            if middle:
                #check for side
                if board[1] == "X" or board[3] == "X" or board[5] == "X" or board[7] =="X":
                    pos = block()
                else:
                    if board[2] == "X":
                        pos = 6
                    elif board[6] == "X":
                        pos = 2
            else:
                if x_1==8:
                    pos = 2
                else:
                    pos = 8     
    elif board.count("-")> len(board)-7:
        pos = check_crit_move()
    elif board.count("-") == 1:
        pos = block()
    return pos

##### checks if you are about to win or lose and returns the position if you are #####
def check_crit_move():
    pos = None
    ctw = close_to_win()
    b = block()
    if ctw!=None:
        pos = ctw
    elif b!=None:
        pos = b
    return pos

##### checks if you're able to win returns positions if able #####
def close_to_win():
    length = len(board)
    i=0
    global game_ongoing
    global difficulty
    if game_ongoing:
        while i < length:
            if board[i] == '-':
                board[i] = 'O'
                if check_win(board)=='O':
                    game_ongoing = False
                    return i
                else:
                    board[i]='-'
            i+=1
    return None

###### Stop a player from winning ######
def block():
    global difficulty
    global game_ongoing
    length = len(board)
    i=0
    if game_ongoing:
        while i < length:
            if board[i] == '-':
                board[i] = 'X'
                if check_win(board)=='O':
                    board[i]='-'
                    return i
                else:
                    board[i]='-'
            i+=1
    return None

##### Game Engine #####
def one_player_game():
    global cp
    global board
    global game_ongoing
    global difficulty
    difficulty = input("Welcome! Select the difficulty of the game (e/m/h): ")
    print('\n')
    print("Game beginning you are X")
    display_board(board)
    if difficulty=='e' or difficulty=='m':
        cp = "X"
    else:
        difficulty='h'
        cp = 'O'
    game_ongoing = True
    while game_ongoing:
        handle_turn(cp)
        game_ongoing = check_game_over(board)
        cp = flip_player(cp)
        display_board(board)
    end_reset(1,difficulty)
    cp = "X"
    board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]
    game_ongoing = True
    