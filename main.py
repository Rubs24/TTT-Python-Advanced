from onePlayer import *
from twoPlayer import *

def choose_game():
    game_choice = input("Would you like to play a one or two player game? (1/2): ")
    
    valid = False
    while not valid:
        if game_choice == "1":
            valid = True
            one_player_game()
        elif game_choice == "2":
            valid = True
            two_player_game()
        else:
            print("Error please enter 1 or 2 (1/2)")
    return 

def play():
    want_to_play = True
    while want_to_play==True:
        choose_game()
        play_again = input( "Would you like to play again? (y/n): ")
        if play_again == "n":
            want_to_play = False
        elif play_again == "y":
            want_to_play = True
        else:
            want_to_play = False
        

play()


            


#Board
#Display
#Play game
#check win -> check rows -> check cols -> check diags
#chekc tie
#flip player