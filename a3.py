#Assignment 3 Tic-Tac-Toe
import random
import copy

def play_a_new_game():
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	

	instructions()
	#display(board)
	#Want player to keep playing until there is a winner:
	turn = input("If you want to go first please type 1, please type 2 if you want to go second. ")
	if int(turn) == 1:
		#Keep playing if board is not full and there is no winner
		while (len(possible_moves(board))!= 0):
			playerpos = input("Please choose a position (1-9) on the board where you would like to place your X \n")
			while(check_valid(board, int(playerpos)) == False):
				playerpos = input("That is not a valid position, please try again. ")
			place_move(board, int(playerpos), "player")
			#After the move has been made check if there is a win
			if(check_winner(board)):
				print("The player wins!!!!!")
				display(board)
				return
			display(board)
			#Computer input and checking if valid
			if(len(possible_moves(board)) == 0):
				print("It's a draw!!")
				return
			print("Now it is the computer's turn \n")
			moves = possible_moves(board)
			cpupos = Monte_Carlo_Tree_Search(board)
			place_move(board, cpupos, "CPU")
			if(check_winner(board)):
				print("The computer wins :(")
				display(board)
				return
			display(board)

	else:
		while (len(possible_moves(board))!= 0):
			print("It is the computer's turn \n")
			moves = possible_moves(board)
			cpupos = Monte_Carlo_Tree_Search(board)
			place_move(board, cpupos, "CPU")
			if(check_winner(board)):
				print("The computer wins :(")
				display(board)
				return
			display(board)

			if(len(possible_moves(board)) == 0):
				print("It's a draw!!")
				return
			playerpos = input("Please choose a position (1-9) on the board where you would like to place your X \n")
			while(check_valid(board, int(playerpos)) == False):
				playerpos = input("That is not a valid position, please try again. ")
			place_move(board, int(playerpos), "player")
			#After the move has been made check if there is a win
			if(check_winner(board)):
				print("The player wins!!!!!")
				display(board)
				return
			display(board)


def instructions():
	print("These are the positions on the board")
	print(" 1 | 2 | 3")
	print("---+---+---")
	print(" 4 | 5 | 6")
	print("---+---+---")
	print(" 7 | 8 | 9")


def check_valid(board, position):
	return board[position-1] == ' '

def possible_moves(board):
	#returns the index where the board is empty 
	moves = []
	for i in range(len(board)):
		if board[i] == " ":
			moves.append(i+1)
	return moves


def place_move(board, position, user):
	if user == "player":
		symbol = "X"
	else:
		symbol = "O"

	board[position-1] = symbol


def check_winner(board):

	#checking rows
	for i in range(0,7,3):
		if board[i] == board[i+1] and board[i+1]== board[i+2] and board[i] != " ":
			return True
	#checking columns
	for i in range (0,3):
		if board[i] == board[i+3] and board[i+3] ==board[i+6] and board[i] != " ":
			return True

	#check diagonals
	if board[0] == board[4] and board[4] == board[8] and board[0] != " ":
		return True
	if board[2] == board[4] and board[4] == board[6] and board[2] != " ":
		return True
	return False



#Current status of the board 
def display(board):
	print(board[0], "|", board[1], "|", board[2])
	print("--+---+--")
	print(board[3], "|", board[4], "|", board[5])
	print("--+---+--")
	print(board[6], "|", board[7], "|", board[8])


def Monte_Carlo_Tree_Search(board):
	#Heuristic that provides the best choice by doing random playouts
	moves = possible_moves(board)
	#make a dictionary of the possible moves
	moves_score = {}
	#length = len(moves)
	for i in moves:
		moves_score.setdefault(i, 0)
	#Looping through each move
	for move in moves:
		#dont want actual change on the play_board2
		play_board = copy.deepcopy(board)
		cpupos = move
		place_move(play_board, cpupos, "CPU")
		#print("This is the board before the play out")
		#display(play_board)
		#print("This is the curernt board before random play outs:")
		#display(play_board2)
		for i in range(1000):
			play_board2 = copy.deepcopy(play_board)
			#print("Playing the board out now")
			#display(play_board2)
			while (len(possible_moves(play_board2))!= 0):
				move_now = possible_moves(play_board2)
				playerpos = random.choice(move_now)
				place_move(play_board2, playerpos, "player")
				if(check_winner(play_board2)):
					moves_score[move] -=10
					#display(play_board2)
					break
				#display(play_board2)

				if(len(possible_moves(play_board2)) == 0):
					moves_score[move] +=5
					break
				move_now = possible_moves(play_board2)
				cpupos = random.choice(moves)
				place_move(play_board2, cpupos, "CPU")
				if(check_winner(play_board2)):
					moves_score[move] +=1
					break
				#display(play_board2)
			#print("This is the end of the play out.")
			#display(play_board2)
		#print("This is the results of move score.")
		#print(moves_score)
	#At the end of the random play out choose one with the biggest score
	max_key = max(moves_score, key=moves_score.get)
	return max_key

if __name__ == '__main__':
	play_a_new_game()


