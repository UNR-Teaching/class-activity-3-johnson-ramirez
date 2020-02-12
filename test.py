import unittest
import tictactoe as BoardClass
import move as MoveClass

class Test_check_inbounds(unittest.TestCase):
	game_board = BoardClass.Board()	

	
	def test_both_valid_equal(self):
		print("Testing valid equal")
		self.assertTrue(self.game_board.check_inbounds(2,2))

	def test_both_valid(self):
		print("Testing both valid")
		self.assertTrue(self.game_board.check_inbounds(2,1))

	def test_both_invalid(self):
		print("Testing both invalid")
		self.assertFalse(self.game_board.check_inbounds(4,4))

	def test_one_valid_one_invalid(self):

		print("Testing valid and invalid")
		self.assertFalse(self.game_board.check_inbounds(4,1))

class Test_check_unoccupied(unittest.TestCase):	
	
	board = BoardClass.Board()	

	def test_unoccupied(self):

		print("Testing unoccupied")
		self.board.game_board[2][2] = '0'
		self.assertTrue(self.board.check_unoccupied(2,2))

	def test_occupied(self):

		print("Testing occupied")
		self.board.game_board[2][2] = 'X'

		self.assertFalse(self.board.check_unoccupied(2,2))


class Test_check_valid_move(unittest.TestCase):	
	
	board = BoardClass.Board()
	
	def test_valid_move(self):

		print("Testing valid")
		testMove = MoveClass.move(2,2,'X')
		self.assertTrue(self.board.check_valid_move(testMove))

	def test_valid_occupied(self):

		print("Testing valid occupied")
		self.board.game_board[2][2] = 'X'

		testMove = MoveClass.move(2,2,'O')

		self.assertFalse(self.board.check_valid_move(testMove))

	def test_invalid(self):

		print("Testing invalid")
		testMove = MoveClass.move(3,3,'O')
		self.assertFalse(self.board.check_valid_move(testMove))



class Test_Has_Winner(unittest.TestCase):

	board = BoardClass.Board()

	def test_Horizontal_Win(self):

		print("Testing horizontal win")

		self.board.game_board = [['0',"X",'0'],['0',"X",'0'],['0',"X",'0']]

		self.assertEqual(self.board.has_winner(), "0")




		
		


if __name__ == '__main__':
	unittest.main()
