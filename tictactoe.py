""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""
from player import *
from move import *

class Board(object):

	def __init__(self):
		"""
        Initializes the Board of size 3x3
        """
		self.game_board = [['0','0','0'],['0','0','0'],['0','0','0']]
		self.count = 0
		self.x_turn = True
	

		pass

	

	def has_winner(self):
		"""
		Checks to see if there is a current winner of the game

		:return: ????
		"""

		"Check for horizonal win"

		for x in range(0, 3):

			if self.game_board[x][0] == self.game_board[x][1] and self.game_board[x][1] == self.game_board[x][2]:

				return self.game_board[x][0]

		"Check for vertical win"

		for y in range(0, 3):

			if self.game_board[0][y] == self.game_board[1][y] and self.game_board[1][y] == self.game_board[2][y]:

				return self.game_board[0][y]

		"Check for diagonal from left to right"
	
		if self.game_board[0][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2]:
			return self.game_board[1][1]	

		if self.game_board[0][2] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][0]:
			return self.game_board[1][1]	

		if self.count == 8:

			return "Tie"

		else:

			return "0"


		pass

	

	def play_game(self, playerX, playerO):
		"""
	 	Takes moves from raw_input as comma-separated list in form (column, row, player)
		and makes a move. When a winner has been determined, the game ends
		    
		:return: (str) the letter representing the player who won
		"""

		result = "0"

		while(result != ("X" or "O" or "Tie")):

			result = take_turn(playerX, playerO, result)

		return result

		pass

	def take_turn(self, playerX, playerO, result):

		if self.count % 2 == 0:

			playerMove = playerX.getMove()

		else:
			playerMove = playerO.getMove()

		if check_valid_move(playerMove):

			self.game_board[playerMove.row][playerMove.column] = playerMove.player

			self.count = self.count + 1

			result = self.has_winner()
		else:
			print("The move that you have made is not valid. Please try again.")

		return result

		pass

	def check_inbounds(self, row, column):

		if 0 < row and row < 3 and 0 < column and column < 3 :
			return True
		else:
			return False

		pass

	def check_unoccupied(self, row, column):

		if self.game_board[row][column] == '0':
			return True
		else:
			return False

		pass

	def check_valid_move(self, move):

		inbounds = self.check_inbounds(move.row, move.column)
		

		if inbounds:
		
			unoccupied = self.check_unoccupied(move.row, move.column)
			if unoccupied:
				return True
			else:
				return False			
		else:
			return False


        
if __name__ == '__main__':
	board = Board()
	
	playerX = Player("X")
	playerO = Player("O")

	winner = board.play_game(playerX, playerO)

	if winner != "Tie":
		
		print("{} has won!".format(winner))
	else:
		print("The game is tied!")	

	
