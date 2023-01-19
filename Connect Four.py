#Python Code for a Connect Four Game 
#===========================
import os

#Constants: 
NUM_COLS = 7
NUM_ROWS = 6
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', "G"]
PLAYER_ICONS = ['X', 'O', 'V', 'M', 'H']
grid = []

#===============================================================================
#Print Grid: Function to print out the Connect 4 Grid
def print_grid(grid): 	
	for letter in LETTERS:    
		print('   ' + letter, end = "")

	print("\n +" + "---+" * NUM_COLS)

	for row in range(NUM_ROWS):    
		print(' |', end = " ")
		for col in range(NUM_COLS):        
			print(grid[row][col] + ' | ', end = "") 
		print("\n +" + "---+" * NUM_COLS)
#===============================================================================
#Update Grid: Function to update the grid depending on the user's input
def update_grid(player, column):
	c = ord(column) - 65 #Converting column (str) to an integer column on the grid
	
	for r in range(NUM_ROWS-1, -2, -1):
		if(r == -1):
			print_grid(grid)
			print("Column is already full! Try another available column!")
			return True

		elif(grid[r][c] == ' '):
			grid[r][c] = PLAYER_ICONS[player]
			print_grid(grid)
			win_checker(r, c, player)
			return False
#===============================================================================
#Player Input: This function will act as the input for Player 1 (X)
def player_input(player): 
	p = input("Player " + str(player+1) + " (" + PLAYER_ICONS[player] + "), " + "Please select a column: ")
	
	while(p not in LETTERS): 
		p = input("Please select a valid column: ")

	return p
#===============================================================================
#Win Checker: This function will constantly check after every input whether a player has won a game
def win_checker(r, c, player):
	#r and c are exactly where the player has placed their marker
	#If they win, we terminate the program here...
	
	#Nested Loops: 
	#If the next one in the chain is X
		#If the next one in the chain is X
			#If the next one in the chain is X
				#You win: Terminate!

	#Have to account for grid boundaries, whether the X is in the middle of a chain etc. 
	#Maybe can use recursion?!? How to keep track of 4 recursive cases?
	#If detetcted a value off grid, then move either only backwards or forwards

	if(grid[r][c] == PLAYER_ICONS[player]):
		if(r+1 > -1 and r+1 < 6):
			win_checker(r+1, c, player)
			
			
		else:
			win_checker(r-1, c, player)
	

#===============================================================================
#MAIN Function:
def main(): 
	print("==============================WELCOME TO CONNECT 4==============================")
	print("Objective: Get 4 in a row to win!")
		
	players = int(input("How many players are playing? (Max. 5 Players): "))
	while(players < 0 or players > 6):
		players = int(input("Please enter a valid number of players: "))
	print("======================================BEGIN=====================================")
	
	#Set up an empty grid:
	for row in range(NUM_ROWS): 
			row_list = []
			for col in range(NUM_COLS):
				row_list.append(' ')
			grid.append(row_list)
	
	#Then we will print the empty grid. 
	print_grid(grid)

	#Now each player will have their turn:
	turns = 0
	
	#If the turns ever equals all possible positions, then the game ends and we break.
	while(turns != NUM_ROWS*NUM_COLS):
		for player in range(players):
			column = player_input(player)
			os.system("clear")
			missed_turn = update_grid(player, column) #player = Player Number // #column = Column that they have chosen
			if(missed_turn == False): turns += 1

			#This ensures that if a column is full, their turn isn't skipped and repeated.
			while(missed_turn == True): 
				column = player_input(player)
				os.system("clear")
				missed_turn = update_grid(player, column) 
				if(missed_turn == False): turns += 1

	if(turns == NUM_COLS*NUM_ROWS): print("Grid has been filled! Game Complete!")
#===============================================================================
#Program Execution:
main()



#Problems that need fixing: 
#1) Create a function that checks whether they have 4 in a row... Idk how to do this but we shall check...
#For this you may need to check, every tile that has X and check if row+1. row+2 and row+3 is full, same logic like that diagonally and vertically too... This is quite inefficient though, maybe a better way?

# I was thinking: 
# Have 4 if else statements nested under each other. So one would be to check if there is a second connection (either vetically horizontally or diagonally)
# Then there would be a third loop for the third connection
# If there was a fourth connection, then we break the entire thing and return true and this will termiante the entire code. 