from move import *
class Player(object):

	def __init__(self, name):
		self.name = name
		

	def getMove(self):
		"""
		Marks a square at coordinate (column, row) for player

		:param column: (int) the 0-indexed column of the Board to mark
		:param row: (int) the 0-indexed row of the Board to mark
		:param player: (str) the X or O representation of which player to mark in square

		:return: ????
		"""
		row = input("Enter a row: ")
		col = input("Enter a column: ")

		playerMove = move(row, col, self.name )
		
		return playerMove
	

		pass
