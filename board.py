import sys

class Board:
	board = []
	yRange = 0
	xRange = 0
	def __init__(self, maze):
		self.parse(maze)
		
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
	
	def findStart(self):
		col = 0
		for column in self.board:
			row = 0
			for tile in column:
				if (tile == "S"):
					return [row,col]
				row +=1
			col += 1	
