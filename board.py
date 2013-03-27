import sys

class Board:
	board = []
	yRange = 0
	xRange = 0
	startPosition = [0,0]
	goalPosition = [1,1]
	def __init__(self, maze):
		self.parse(maze)
		startPosition = self.getStart()
		goalPosition = self.getGoal()
	# Parse a file and return a board 
	def parse(self,maze):
		mazeBoard = open(maze,'r')
		for line in mazeBoard:
			loc = 0
			column = []
			while loc < len(line):
				column += line[loc]
				loc += 1
			self.board.append(column)
	
	def getStart(self):
		for y in xrange(self.yRange + 1):
			for x in xrange(self.xRange + 1):
				if board[y][x] == 'START':
					return [y][x]
	def getGoal(self):
		for y in xrange(self.yRange + 1):
			for x in xrange(self.xRange + 1):
				if board[y][x] == 'GOAL':
					return [y][x]
	def boardDisplay(self):
		for y in xrange(yRange + 1):
			for x in xrange(xRange + 1):
				if board[y][x] == 'START':
					sys.stdout.write('S')
				if board[y][x] == 'OPEN':
					sys.stdout.write('.')
				if board[y][x] == 'GOAL':
					sys.stdout.write('G')
				if board[y][x] == 'BARRIER':
					sys.stdout.write('*')
			sys.stdout.write('\n')
			
	def isBarrier(self,position):
		if self.board[position[0]][position[1]] == 'BARRIER':
			return True
	def isGoal(self,position):
		if self.board[position[0]][position[1]] == 'GOAL':
			return True	
