quit# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:16:32 2018

@author: James Lewis
"""

""" 
Program (CONNECT 5)
"""

from sys import platform

# Color Initialization
from colored import fg, attr

# Import OS clear screen 

import os

# Global Variables
    
board = [' '] * 55
game_state = True
announce = ''

# Create Clear Function
def clr():
    if platform == 'win32': 
        os.system('cls')
    if platform == 'linux':
        os.system('clear')
        

# Reset Board Function

def reset_board():
    global board,game_state
    board = [' '] * 55
    game_state = True

# Display Board Function for connect 5

def display_board():
    ''' This function prints out the board, numbers 1-81 will be used to reference the spots!'''
    ct = fg(124)
    cn = fg(32)
    c = fg(238)
    rs = attr('reset')
    # Clear current cell output
    clr()
    # Print board
    print("   ")
    print(ct+"    'Connect 5'"+cn+" by James M. Lewis!"+rs)
    print("   ")
    print('    Please select a number between 1 & 54.')
    print( "    *************************************")
    print( "    *"+" "+ c +"1"+ rs +" | "+c+"2"+rs+" | "+c+"3"+rs+" | "+c+"4"+rs+" | "+c+"5"+rs+" | "+c+"6"+rs+" | "+c+"7"+rs+" | "+c+"8"+rs+" | "+c+"9"+rs+" "+"*" )
    print( "    *"+" "+board[1]+" | "+board[2]+" | "+board[3]+" | "+board[4]+" | "+board[5]+" | "+board[6]+" | "+board[7]+" | "+board[8]+" | "+board[9]+" "+"*" )
    print( "    *"+"-----------------------------------"+"*" )
    print( "    *"+" "+c+"10"+rs+"| "+c+"11"+rs+"| "+c+"12"+rs+"| "+c+"13"+rs+"| "+c+"14"+rs+"| "+c+"15"+rs+"| "+c+"16"+rs+"| "+c+"17"+rs+"| "+c+"18"+rs+"*" )
    print( "    *"+" "+board[10]+" | "+board[11]+" | "+board[12]+" | "+board[13]+" | "+board[14]+" | "+board[15]+" | "+board[16]+" | "+board[17]+" | "+board[18]+" "+"*" )
    print( "    *"+"-----------------------------------"+"*" )
    print( "    *"+" "+c+"19"+rs+"| "+c+"20"+rs+"| "+c+"21"+rs+"| "+c+"22"+rs+"| "+c+"23"+rs+"| "+c+"24"+rs+"| "+c+"25"+rs+"| "+c+"26"+rs+"| "+c+"27"+rs+"*" )
    print( "    *"+" "+board[19]+" | "+board[20]+" | "+board[21]+" | "+board[22]+" | "+board[23]+" | "+board[24]+" | "+board[25]+" | "+board[26]+" | "+board[27]+" "+"*" )
    print( "    *"+"-----------------------------------"+"*" )
    print( "    *"+" "+c+"28"+rs+"| "+c+"29"+rs+"| "+c+"30"+rs+"| "+c+"31"+rs+"| "+c+"32"+rs+"| "+c+"33"+rs+"| "+c+"34"+rs+"| "+c+"35"+rs+"| "+c+"36"+rs+"*" )
    print( "    *"+" "+board[28]+" | "+board[29]+" | "+board[30]+" | "+board[31]+" | "+board[32]+" | "+board[33]+" | "+board[34]+" | "+board[35]+" | "+board[36]+" "+"*" )
    print( "    *"+"-----------------------------------"+"*" )
    print( "    *"+" "+c+"37"+rs+"| "+c+"38"+rs+"| "+c+"39"+rs+"| "+c+"40"+rs+"| "+c+"41"+rs+"| "+c+"42"+rs+"| "+c+"43"+rs+"| "+c+"44"+rs+"| "+c+"45"+rs+"*" )
    print( "    *"+" "+board[37]+" | "+board[38]+" | "+board[39]+" | "+board[40]+" | "+board[41]+" | "+board[42]+" | "+board[43]+" | "+board[44]+" | "+board[45]+" "+"*" )
    print( "    *"+"-----------------------------------"+"*" )
    print( "    *"+" "+c+"46"+rs+"| "+c+"47"+rs+"| "+c+"48"+rs+"| "+c+"49"+rs+"| "+c+"50"+rs+"| "+c+"51"+rs+"| "+c+"52"+rs+"| "+c+"53"+rs+"| "+c+"54"+rs+"*" )
    print( "    *"+" "+board[46]+" | "+board[47]+" | "+board[48]+" | "+board[49]+" | "+board[50]+" | "+board[51]+" | "+board[52]+" | "+board[53]+" | "+board[54]+" "+"*" )
    print( "    *************************************")
    
# Win check for Connect 5 game.

def win_check(board, player):
    """ Check all possible horizontal, diaganal and vertical possibilities for a win."""
    
    """Check Horizontal Rows for Win """
    if (board[1] == board[2] == board[3] == board[4] == board[5] == player) or \
        (board[2] == board[3] == board[4] == board[5] == board[6] == player) or \
        (board[3] == board[4] == board[5] == board[6] == board[7] == player) or \
        (board[4] == board[5] == board[6] == board[7] == board[8] == player) or \
        (board[5] == board[6] == board[7] == board[8] == board[9] == player) or \
        (board[10] == board[11] == board[12] == board[13] == board[14] == player) or \
        (board[11] == board[12] == board[13] == board[14] == board[15] == player) or \
        (board[12] == board[13] == board[14] == board[15] == board[16] == player) or \
        (board[13] == board[14] == board[15] == board[16] == board[17] == player) or \
        (board[14] == board[15] == board[16] == board[17] == board[18] == player) or \
        (board[19] == board[20] == board[21] == board[22] == board[23] == player) or \
        (board[20] == board[21] == board[22] == board[23] == board[24] == player) or \
        (board[21] == board[22] == board[23] == board[24] == board[25] == player) or \
        (board[22] == board[23] == board[24] == board[25] == board[26] == player) or \
        (board[23] == board[24] == board[25] == board[26] == board[27] == player) or \
        (board[28] == board[29] == board[30] == board[31] == board[32] == player) or \
        (board[29] == board[30] == board[31] == board[32] == board[33] == player) or \
        (board[30] == board[31] == board[32] == board[33] == board[34] == player) or \
        (board[31] == board[32] == board[33] == board[34] == board[35] == player) or \
        (board[32] == board[33] == board[34] == board[35] == board[36] == player) or \
        (board[37] == board[38] == board[39] == board[40] == board[41] == player) or \
        (board[38] == board[39] == board[40] == board[41] == board[42] == player) or \
        (board[39] == board[40] == board[41] == board[42] == board[43] == player) or \
        (board[40] == board[41] == board[42] == board[43] == board[44] == player) or \
        (board[41] == board[42] == board[43] == board[44] == board[45] == player) or \
        (board[46] == board[47] == board[48] == board[49] == board[50] == player) or \
        (board[47] == board[48] == board[49] == board[50] == board[51] == player) or \
        (board[48] == board[49] == board[50] == board[51] == board[52] == player) or \
        (board[49] == board[50] == board[51] == board[52] == board[53] == player) or \
        (board[50] == board[51] == board[52] == board[53] == board[54] == player) or \
        (board[1] == board[10] == board[19] == board[28] == board[37] == player) or \
        (board[10] == board[19] == board[28] == board[37] == board[46] == player) or \
        (board[2] == board[11] == board[20] == board[29] == board[38] == player) or \
        (board[11] == board[20] == board[29] == board[38] == board[47] == player) or \
        (board[3] == board[12] == board[21] == board[30] == board[39] == player) or \
        (board[12] == board[21] == board[30] == board[39] == board[48] == player) or \
        (board[4] == board[13] == board[22] == board[31] == board[40] == player) or \
        (board[13] == board[22] == board[31] == board[40] == board[49] == player) or \
        (board[5] == board[14] == board[23] == board[32] == board[41] == player) or \
        (board[14] == board[23] == board[32] == board[41] == board[50] == player) or \
        (board[6] == board[15] == board[24] == board[33] == board[42] == player) or \
        (board[15] == board[24] == board[33] == board[42] == board[51] == player) or \
        (board[7] == board[16] == board[25] == board[34] == board[43] == player) or \
        (board[16] == board[25] == board[34] == board[43] == board[52] == player) or \
        (board[8] == board[17] == board[26] == board[35] == board[44] == player) or \
        (board[17] == board[26] == board[35] == board[44] == board[53] == player) or \
        (board[9] == board[18] == board[27] == board[36] == board[45] == player) or \
        (board[18] == board[27] == board[36] == board[45] == board[54] == player) or \
        (board[1] == board[11] == board[21] == board[31] == board[41] == player) or \
        (board[10] == board[20] == board[30] == board[40] == board[50] == player) or \
        (board[2] == board[12] == board[22] == board[32] == board[42] == player) or \
        (board[11] == board[21] == board[31] == board[41] == board[51] == player) or \
        (board[3] == board[13] == board[23] == board[33] == board[43] == player) or \
        (board[12] == board[22] == board[32] == board[42] == board[52] == player) or \
        (board[4] == board[14] == board[24] == board[34] == board[44] == player) or \
        (board[13] == board[23] == board[33] == board[43] == board[53] == player) or \
        (board[5] == board[15] == board[25] == board[35] == board[45] == player) or \
        (board[14] == board[24] == board[34] == board[44] == board[54] == player) or \
        (board[5] == board[13] == board[21] == board[29] == board[37] == player) or \
        (board[14] == board[22] == board[30] == board[38] == board[46] == player) or \
        (board[6] == board[14] == board[22] == board[30] == board[38] == player) or \
        (board[15] == board[23] == board[31] == board[39] == board[47] == player) or \
        (board[7] == board[15] == board[23] == board[31] == board[39] == player) or \
        (board[16] == board[24] == board[32] == board[40] == board[48] == player) or \
        (board[8] == board[16] == board[24] == board[32] == board[40] == player) or \
        (board[17] == board[25] == board[33] == board[41] == board[49] == player) or \
        (board[9] == board[17] == board[25] == board[33] == board[41] == player) or \
        (board[18] == board[26] == board[34] == board[42] == board[50] == player):
        return True
    else:
        return False
    
# Full board Check
        
def full_board_check(board):
    if " " in board[1:]:
        return False
    else:
        return True

# Ask Player where to place their mark!
def ask_player(mark):
    """ Asks Player where to place X OR O, checks validity!"""
    global board
    while True:
        req = '    Place your mark: Player ' + mark + ' '
              
        try:
            choice = int(input(req))
        except ValueError:
            print("    Sorry, please input a number between 1-54.")
            continue
        if choice not in range(1,55):
            print("    Sorry, please input a number between 1-54.")
            continue
        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print( "    Please choose another Space, one that is empty!" )
            continue
        
# Player Choice      
def player_choice(mark):
    global board,game_state,announce
    #Set game blank game announcement
    announce = ''
    #Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for player win
    if win_check(board,mark):

        display_board()
        announce = "    "+ "Player " + mark +" wins! Congratulations"
        game_state = False
    
    #Show board
    clr()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
        
    return game_state,announce

def play_game():
    print("    Welcome to Connect 5!")
    reset_board()
    global announce
    
    xc = fg(46)
    oc = fg(207)
    rs = attr('reset')
    # Set marks
    X= xc + 'X' + rs
    O= oc + 'O' + rs
    while True:
        # Show board
        display_board()
        
        # Player X turn
        game_state,announce = player_choice(X)
        print(announce)
        if game_state == False:
            break
            
        # Player O turn
        game_state,announce = player_choice(O)
        print(announce)
        if game_state == False:
            break
    
    # Ask player for a rematch
    rematch = input('    Play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print("    Thanks for playing!")

play_game()

 
