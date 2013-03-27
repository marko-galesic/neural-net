import sys

class Board:
	board = []
	yRange = 0
	xRange = 0
	startPosition = [0,0]
	goalPosition = [1,1]
	def __init__(self, maze):
		self.parse(maze)
		self.startPosition = self.getStart()
		self.goalPosition = self.getGoal()
	# Parse a file and return a board 
	def parse(self,maze):
		mazeBoard = open(maze,'r')
		for line in mazeBoard:
			loc = 0
			column = []
			while loc < len(line):
				s = line[loc]
				if (s == "S"):
					s = "START"
				elif(s == "G"):
					s = "GOAL"
				elif(s == "."):
					s = "OPEN"
				elif(s =="*"):
					s = "BARRIOR"
				if(s != "\n"):
					column.append(s)
				loc += 1
				xRange = len(line)
			self.board.append(column)
		yRange = len(self.board)
	
	def getStart(self):
		y = 0
		while y < len(self.board):
			x = 0
			while x < len(self.board[y]):
				if self.board[y][x] == 'START':
					return [y,x]
				x+= 1
			y += 1

	def getGoal(self):
		for y in xrange(self.yRange + 1):
			for x in xrange(self.xRange + 1):
				if self.board[y][x] == 'GOAL':
					return [y][x]
	def boardDisplay(self):
		y = 0
		board = self.board
		while y < len(board):
			x = 0
			while x < len(board[y]):
				if board[y][x] == 'START':
					sys.stdout.write('S')
				if self.board[y][x] == 'OPEN':
					sys.stdout.write('.')
				if self.board[y][x] == 'GOAL':
					sys.stdout.write('G')
				if self.board[y][x] == 'BARRIER':
					sys.stdout.write('*')
				x+=1
			y += 1
			sys.stdout.write('\n')
			
	def isBarrier(self,position):
		print "Y: " + str(position[1])
		print "X: " + str(position[0])
		if self.board[position[0]][position[1]] == 'BARRIER':
			return True
		return False
	def isGoal(self,position):
		if self.board[position[0]][position[1]] == 'GOAL':
			return True	
		return False
