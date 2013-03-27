from die import Die
from board import Board

class Game:

	board = None
	die = None
	position = None

	def __init__(self,file):
		self.die = Die()				# Die our pet ai will play with
		self.board = Board(file)		# Game board our pet ai will play with
		self.position = self.board.getStart()		# Cartesian position of die
