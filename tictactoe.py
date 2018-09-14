#tictactoe



import random
import os
import time


#the AI plays as O and the human plays as X

#main Board class

class Board():

	def __init__(self):

		#the board variable
		self.board = ['', '', '', '', '', '', '', '', '']

		#combinations for winning
		self.winning_combo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

		#index for the 9 positions on the board
		self.index = [0,1,2,3,4,5,6,7,8]

		#bot movements
		self.bot_moves = 0



	#function to show board
	def show_status(self):

		print('this is the board')
		print()
		print('{0}  | {1}  | {2}'.format(self.board[0], self.board[1], self.board[2]))
		print('_________')
		print('{0}  | {1}  | {2}'.format(self.board[3], self.board[4], self.board[5]))
		print('_________')
		print('{0}  | {1}  | {2}'.format(self.board[6], self.board[7], self.board[8]))



	#function to update board
	def update_status(self, place, player):

		if self.board[place] == '':  #ie if the board position - corresponding to the [place] - is empty
			self.board[place] = player #where human player is X and the AI is O
		else:
			return



	#function to check for a win
	def check_win(self, player):

		for x,y,z in self.winning_combo:
			if self.board[x] == self.board[y] == self.board[z] == player:
				return True
				break


	#function to award a draw
	def draw(self):

		filled = []
		for i in self.index:
			if self.board[i] != '':
				filled.append(i)
		if len(filled) == 9:
			return True



	#function to select position for bot
	def bot_turn(self):

		moved = False
		first_corner = None


		#bot checks for a win in next turn
		for x,y,z in self.winning_combo:
			if self.board[x] == 'O' and self.board[y] == 'O' and self.board[z]=='':
				return z
				break
				moved=True

			if self.board[x] == '' and self.board[y] == 'O' and self.board[z]=='O':
				return x
				break
				moved=True

			if self.board[x] == 'O' and self.board[y] == '' and self.board[z]=='O':
				return y
				break
				moved=True



		#bot blocks player
		for x,y,z in self.winning_combo:
			if self.board[x]=='X' and self.board[y]=='X' and self.board[z]=='':
				return z
				break
				moved=True

			if self.board[x]=='' and self.board[y]=='X' and self.board[z]=='X':
				return x
				break
				moved=True

			if self.board[x]=='X' and self.board[y]=='' and self.board[z]=='X':
				return y
				break
				moved=True



		#bot chooses position 4 as its position if position 4 is empty and if bot is about to make its first move
		if self.bot_moves==0 and moved==False and self.board[4]=='':
			return 4

		#if self.bot_moves==0 and moved==False:
			#if self.board[4]=='':
				#return 4
				#break
				#moved = True


		#bot chooses any empty position
		for i in self.index:
			if self.board[i] == '':
				return i


#create board object
board = Board()


#create a function to refresh terminal and show board status
def refresh_screen():
	os.system('clear')
	board.show_status()
	print()



#begin game
print('Welcome to Tic Tac Toe!\n')



#main game loop
while 1:
	refresh_screen()


	## HUMAN HAS A TURN ##


	#request choice of player position
	player_position = int(input('choose position from 0 to 8:  '))


	#update board with 'X' in player's position
	board.update_status(player_position, 'X')


	refresh_screen()


	#check for a human win
	if board.check_win('X'):
		refresh_screen()
		print('human wins!!')
		break


	#check for a tie
	if board.draw():
		refresh_screen()
		print('it\'s a draw!!!')
		break




	
	## BOT HAS A TURN ##


	#take positional integer returned by bot_turn function and assign it to a bot_position variable

	
	bot_position = board.bot_turn()


	#update the board with the bot's position
	board.update_status(bot_position, 'O')


	#bot has made a move, therefore increment bot_moves variable by 1
	board.bot_moves += 1	


	#check for a bot win
	if board.check_win('O'):
		refresh_screen()
		print('bot wins!!!')
		break


	#check for a draw
	if board.draw():
		refresh_screen()
		print('draw!!!')
		break