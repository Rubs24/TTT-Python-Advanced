from scores import new_score
game_ongoing=True
winner = None
current_player = None

def display_board(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

def check_win(b):
    global winner
    global current_player
    col_win = check_cols(b)
    diag_win = check_diag(b)
    row_win = check_rows(b)
    if row_win or col_win or diag_win:
        winner = current_player
    else:
        winner = None
    return winner

def check_rows(board):
    global game_ongoing
    global current_player
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        return current_player
    return
    
def check_cols(board):
    global game_ongoing
    global current_player
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        return current_player
    return

def check_diag(board):
    global game_ongoing
    global current_player
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        return current_player
    return

def check_tie(board):
    global game_ongoing
    if "-" not in board:
        game_ongoing = False
    return 

def flip_player(cp):
    global current_player
    if cp == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_player

def check_game_over(b):
    global game_ongoing
    winner = check_win(b)
    if winner != None:
        game_ongoing = False
    check_tie(b)
    return game_ongoing

def end_reset(game_type,diff=''):
    global board
    global game_ongoing
    game_ongoing = True
    #game has ended
    
    if(game_type==1 and winner == "O"):
        print('O WON!')
        print()
        new_score('AI'+diff)
    elif(game_type==1 and winner == "X"):
        print()
        init = input("YOU WON! Please Enter 3 Initials: ")
        new_score(init[:3])
    elif(game_type==2 and winner != None):
        print(winner+" WON!")
        print()
        init = input('Please Enter 3 Initials: ')
        new_score(init[:3])
    else:
        print("Tie")
        print()
        new_score('TIE')
    board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]
    print()