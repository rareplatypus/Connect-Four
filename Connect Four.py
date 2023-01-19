import os
import random

BOARD_ROW = 5
BOARD_COL = 5
PLAYER_NUM = 3
VARIABLES1 = ["O", "X", "V", "H", "M"]
VARIABLES = VARIABLES1[:PLAYER_NUM]
random.shuffle(VARIABLES)
WIN_CON = 4
count = -1

# marking how many marks are in each column
stack = []
for col in range(BOARD_COL):
	stack.append(BOARD_ROW - 1)

# create the inner board
inner_board = []
for row in range(BOARD_ROW):
	col_list = []
	for col in range(BOARD_COL):
		col_list.append(" ")
	inner_board.append(col_list)

# create the outer board
outer_board = []
for row in range(BOARD_ROW):
	col_list = []
	for col in range(BOARD_COL):
		col_list.append(" ")
	outer_board.append(col_list)

# function for printing
def print_board():
	for alphabet in range(BOARD_COL):
		print("  " + chr(65 + alphabet) + " ", end = "")

	print("\n+" + "---+"*BOARD_COL, end = "")

	for row in range(BOARD_ROW):
		print("\n|", end = "")
		for col in range(BOARD_COL):
			print(" " + inner_board[row][col] + " |", end = "")
		print("\n+" + "---+"*BOARD_COL, end = "")

# print the outer board of the first time
print_board()
print()

# Selecting players and sequence
for items in range(PLAYER_NUM):
	print("Player", VARIABLES[items], "goes", items + 1)

# print the winning condition
print("Match", WIN_CON, "checkers to win the game")

validity = True
while validity == True:
	# user input location
	temp = input("\nInput a column: ")

	# check if the location is valid
	# # try exception handle
	location = 0
	if len(temp) == 1 and temp.isdigit() == False and 0 <= ord(temp) - 65 < BOARD_COL:
		location = ord(temp) - 65

		# change the inner board
		if 0 <= stack[location]:
			count = count + 1
			inner_board[stack[location]][location] = VARIABLES[count % PLAYER_NUM]
			
			# mark that that column increase 1 unit
			stack[location] = int(stack[location]) - 1
		
			# clear the screen
			os.system("clear")

			# print the outer board
			print_board()

			# check the condition of draw
			if count + 1 == BOARD_COL*BOARD_ROW:
				print("\nGAMEOVER, DRAW!")
				break

			# check if a line is made with the inner board
			# # horizontally
			match_times = 0
			for row in range(BOARD_ROW):
				if validity == False:
					break
				for col in range(BOARD_COL):
					if inner_board[row][col] == VARIABLES[count % PLAYER_NUM]:
						match_times = match_times + 1
						if match_times == WIN_CON:
							validity = False
							print("\nPlayer", VARIABLES[count % PLAYER_NUM], "wins the game!")
							break
					else:
						match_times = 0
			# # vertically
			match_times = 0
			for col in range(BOARD_COL):
				if validity == False:
					break
				for row in range(BOARD_ROW):
					if inner_board[row][col] == VARIABLES[count % PLAYER_NUM]:
						match_times = match_times + 1
						if match_times == WIN_CON:
							validity = False
							print("\nPlayer", VARIABLES[count % PLAYER_NUM], "wins the game!")
							break
					else:
						match_times = 0
			
			# # diagonally
			match_times = 0
			for row in range(BOARD_ROW - 1,-1,-1):
				if validity == False:
					break
				for col in range(BOARD_COL):
					if row + col < BOARD_ROW:
						if inner_board[row + col][col] == VARIABLES[count % PLAYER_NUM]:
							match_times = match_times + 1
							if match_times == WIN_CON:
								validity = False
								print("\nPlayer", VARIABLES[count % PLAYER_NUM], "wins the game!")
								break
					else:
						match_times = 0
			
			match_times = 0
			for row in range(BOARD_ROW - 1, -1, -1):
				for col in range(BOARD_COL):
					if validity == False:
							break
					if row + col < BOARD_ROW:
						if inner_board[row + col][BOARD_COL - 1 - col] == VARIABLES[count % PLAYER_NUM]:
							match_times = match_times + 1
							if match_times == WIN_CON:
								validity = False
								print("\nPlayer", VARIABLES[count % PLAYER_NUM], "wins the game!")
								break
					else:
						match_times = 0

		else:
			count = count + 1
			print("This column is full!\n")	
	else:
		print("Your input is incorrect!")
