from die import Die
from board import Board

class Game:

	board = None
	die = None
	position = None

	def __init__(self):
		self.die = Die()				# Die our pet ai will play with
	def setUpBoard(self, fileName):
		self.board = Board(fileName)										# Game board our pet ai will play with
		self.position = playerSpace(self.board, self.board.getStart())		# Cartesian position of die

	def setBoard(self,board,position):
		self.board = board
		self.position = position
