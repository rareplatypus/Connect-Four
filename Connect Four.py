import os
import random

#Constants: 
BOARD_ROW = 5
BOARD_COL = 5
WIN_CON = 4
ICONS = ['X', 'O', 'V', 'M', 'H']
#==============================================================================================================================
#1) Column_Space is a list that keeps track of how much space is left in every column:
column_space = []
for col in range(BOARD_COL):
    column_space.append(BOARD_ROW - 1)

#2) Board Setup: 
board = []
for row in range(BOARD_ROW):
    row_list = []
    for col in range(BOARD_COL):
        row_list.append(" ")
    board.append(row_list) 
#==============================================================================================================================
#This function is used to print out the entire board
def print_board():
    for alphabet in range(BOARD_COL):
        print("  " + chr(65 + alphabet) + " ", end = "")
    
    print("\n+" + "---+"*BOARD_COL, end = "")

    for row in range(BOARD_ROW):
        print("\n|", end = "")
        for col in range(BOARD_COL):
            print(" " + board[row][col] + " |", end = "")
        print("\n+" + "---+"*BOARD_COL, end = "")
#==============================================================================================================================
#This function will ensure that the user input is valid:
def user_input(column):
    if((len(column) == 1) and (column.isdigit() == False) and (0 <= ord(column) - 65 < BOARD_COL)):
        return(ord(column) - 65)
    
    else:
        print("This is an invalid input! \n")
        return -1

#==============================================================================================================================
#This function checks if the user has connected 4 in-a-row in all directions (vertically, horizontally, diagonally):
def win_check(player):

    #Horizontally:
    matches = 0
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col] == ICONS[player]:
                matches += 1
                
                #If match_times is the Winning Condition, a player has clearly won, hence we can switch off the game:
                if matches == WIN_CON: 
                    print("Horizontal Win!")
                    print("Player", (player+1), "wins the game!")
                    exit()
            
            else:
                matches = 0

    #Vertically: 
    matches = 0
    for col in range(BOARD_COL):
        for row in range(BOARD_ROW):
            if board[row][col] == ICONS[player]:
                matches += 1
                
                #If match_times is the Winning Condition, a player has clearly won, hence we can switch off the game:
                if matches == WIN_CON: 
                    print("Vertical Win!")
                    print("Player", (player+1), "wins the game!")
                    exit()
            
            else:
                matches = 0

    #Diagonally (bothways):
    matches = 0
    for row in range(BOARD_ROW - 1,-1,-1):
        for col in range(BOARD_COL):
            if row + col < BOARD_ROW:
                if board[row + col][col] == ICONS[player]:
                    matches += 1
                    
                    if matches == WIN_CON:
                        print("Diagonal 1 Win!")
                        print("Player", (player+1), "wins the game!")
                        exit()
            else:
                matches = 0
    
    matches = 0
    for row in range(BOARD_ROW - 1, -1, -1):
        for col in range(BOARD_COL):
            if row + col < BOARD_ROW:
                if board[row + col][BOARD_COL - 1 - col] == ICONS[player]:
                    matches += 1
                    
                    if matches == WIN_CON:
                        print("Diagonal 2 Win!")
                        print("Player", (player+1), "wins the game!")
                        exit()
            else:
                matches = 0

    #Return false by default
    return False
#==============================================================================================================================
#Main Function: 
def main():
    os.system("clear") 
    count = 0

    #Printing the beginning of the program:
    print("============================== Welcome to Connect 4! ==============================")
    players = int(input("How many players are playing? (Max. 5): "))
    while(players <= 0 or players > 6):
        players = int(input("Please enter a valid number of players (Max. 5 Players: "))
    print()
    print("=====================================BEGIN=========================================")

    #Print the board for the first time:
    print_board()
    print()

    #Print the players (and their respective icons) as well as the winning condition:
    for items in range(players):
        print("Player", (items+1), "has the icon:", ICONS[items]) 

    print("How to Win: Match", WIN_CON, "checkers to win the game!\n")

    #This ensures that all the turns are accounted for on the board. 
    while(True):
        #User makes an input:
        for player in range(players):
            Continue = True
            while(Continue): #Continue ensures that if a column is full, the same player repeats their turn
                Continue = False
                str_display = "Player " + str(player+1) + " (" + str(ICONS[player]) + "), " + "Please enter a valid column: "
                player_input = user_input(input(str_display))

                while(player_input == -1):
                    player_input = user_input(input(str_display))

                #Checking if the column has space to put another ICON. 
                #If so, it will take the ICON (of the appropriate player) and place it on the grid column.
                if 0 <= column_space[player_input]:
                    #print("Before:", column_space[player_input], "\n")
                    count += 1
                    board[column_space[player_input]][player_input] = ICONS[player]
                    
                    #Decrement the column space from the stack list:
                    column_space[player_input] = int(column_space[player_input]) - 1
                    #print("After:", column_space[player_input], "\n")

                else:
                    print("This column is full!\n")
                    Continue = True	 
            
            #Clear the screen and print the board once more: 
            os.system("clear")
            print_board()
            print()

            #Condition is all squares are filled and no one won, then we break out of this loop
            if(count == BOARD_COL*BOARD_ROW): break

            #If a player wins the game, then we terminate the program
            win_check(player)
        
        #This is the condition for a draw, if so then we break out of the loop and terminate.
        if(count == BOARD_COL*BOARD_ROW):
            print("\nGAMEOVER! IT IS A DRAW!")
            break
#==============================================================================================================================
#Program execution here: 
main()
