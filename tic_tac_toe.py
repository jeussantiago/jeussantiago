# -*- coding: utf-8 -*-
"""
This program will play Tic Tac Toe between 2 players on a 3 x 3 board

"""
import itertools
import time


def print_board(board):
    for row in board:
        print(row)
 
def update_board(board, row, col, rank):
    board[row][col] = rank

def check_if_space_free(board, row, col, rank):
    if isinstance(board[row][col], int):
        update_board(board, row, col, rank)
        return True
    else: #space is already taken
        print("Space is already occupied." )
        return False

#gets the column position
def what_col_postion(num):
    col = (num % 3) - 1
    if col < 0:
        col = 2
    return col

#gets the row and column position on board
def get_row_col(num = 0):
    row = 0
    col = 0

    if position_input >= 7: #top row
        row = 0 
        col = what_col_postion(position_input)
    elif position_input >= 4: # middle row
        row = 1 
        col = what_col_postion(position_input)
    else: #bottom row
        row = 2
        col = what_col_postion(position_input)
    
    return row, col 

#determine if board is full and there is no winner
def is_full_board(board): 
    for row in board:
        for col in row:
            if not isinstance(col, str):
                return False
    print("Tie Game -_-")
    return True


#determine if there is horizontal winner
def winner_horizontally(board):
    for row in board:
#        print(row)
#        print(row.count(row[0]))
#        print(len(row))
        if all(x == row[0] for x in row):
            return True
    return False

#determine if there is vertical winner
def winner_vertically(board):
    for col in range(len(board)):
        check = []
        for row in board:
           check.append(row[col])
#        print(check)
        if all(x == check[0] for x in check):
            return True
    return False

#determine if there is digonal winner
def winner_diagonally(baord):
    #check for winner backslash style
    check = []
    for count, row in enumerate(board):
        check.append(row[count])
    if all(x == check[0] for x in check):
        return True

    #check for winner fowardslash style
    check = []
    for col, row in enumerate(reversed(range(len(board)))):
        check.append(board[row][col])
    if all(x == check[0] for x in check):
        return True
    return False

def check_if_winner(current_player, board):
    if winner_horizontally(board):
        print("{} has won horizontally!!!".format(current_player))
        return True
    elif winner_vertically(board):
        print("{} has won vertically!!!".format(current_player))
        return True
    elif winner_diagonally(board):
        print("{} has won diagonally!!!".format(current_player))
        return True
    else: #no winner yet
        return False


play = True
while play:
    # player with 'X' always plays first
    p1 = input("Does player 1 want to be 'X' or 'O'? ").upper()
    p2 = 'X'
    if p1 == 'X':
        p2 = 'O'
        player_rank_cycle = itertools.cycle([p1, p2]) 
        player_cycle = itertools.cycle(["player 1", "player 2"])
    else:
        player_rank_cycle = itertools.cycle([p2, p1]) 
        player_cycle = itertools.cycle(["player 2", "player 1"])
    print("player 1: {}  Player 2: {}".format(p1, p2))
    
    board = [[7, 8, 9],
             [4, 5, 6],
             [1, 2, 3]]
    print_board(board)
    in_progress = True
    #play the game
    while in_progress:
        print('---------------------------------------------')
#       for visuals, just so player knows who's turn it is
        current_rank = next(player_rank_cycle)
        current_player = next(player_cycle)
        print("Current Player: {}".format(current_player))
#       print("Current Rank: {}".format(current_rank))
        #check for valid input
        valid_input = True
        try:
            position_input = int(input("Where would you like to place your piece? "))
            if position_input == 0:
                in_progress = False
                print("Game Terminated. Thanks for playing.")
                break
            elif position_input not in range(1, 10): #if not within range
                print('Input not a possible option on the board.')
                #the same player must go again
                valid_input = False
                current_rank = next(player_rank_cycle)
                current_player = next(player_cycle)
        except ValueError:# if not a number
            #the same player must go again
            print('Invalid Input. Numbers only.')
            valid_input = False
            current_rank = next(player_rank_cycle)
            current_player = next(player_cycle)
        except Exception:
            #the same player must go again
            print('Something went wrong')
            valid_input = False
            current_rank = next(player_rank_cycle)
            current_player = next(player_cycle)
        
        #get row, col position of player input and update board
        if valid_input:
            row, col = get_row_col(position_input)
#               print("Row: {}  Column: {}".format(row, col))
            valid_input = check_if_space_free(board, row, col, current_rank)
            if valid_input == False:
                #the same player must go again
                current_rank = next(player_rank_cycle)
                current_player = next(player_cycle)
        
        #print updated board
        print_board(board)
        #check if there is winner or if no more moves can be made
        if check_if_winner(current_player, board) or is_full_board(board):
            print("Thank you for playing.")
            in_progress = False




    #if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        print("See you next time.")
        play = False
    elif play_again == "y":
        print("Restarting....")
        #time delay for effect
        time.sleep(2)
        play = True
    else: 
        print("That wasn't one of the choices. Goodbye. :)")
        play = False


#("Row: {}  Column: {}".format(row, col))
   
        
        
        
        
        
        
        
        
        
        
        
        