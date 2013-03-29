import sys

class Board:
	#[State,[die,cost]]
	board = []
	yRange = 0
	xRange = 0
	startPosition = [0,0]
	goalPosition = [1,1]
	def __init__(self, maze):
		if(type(maze) == type([])):
			self.board = maze
		else:
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
					column.append([s,[]])
				loc += 1
				self.xRange = len(line)
			self.board.append(column)
		self.yRange = len(self.board)
	
	def getStart(self):
		y = 0
		while y < len(self.board):
			x = 0
			while x < len(self.board[y]):
				if self.board[y][x][0] == 'START':
					return [y,x]
				x+= 1
			y += 1

	def getGoal(self):
		for y in xrange(self.yRange + 1):
			for x in xrange(self.xRange + 1):
				if self.board[y][x][0] == 'GOAL':
					return [y, x]
	def boardDisplay(self):
		y = 0
		board = self.board
		print("############")
		while y < len(board):
			x = 0
			while x < len(board[y]):
				if board[y][x][0] == 'START':
					sys.stdout.write('S')
				elif self.board[y][x][0] == 'OPEN':
					sys.stdout.write('.')
				elif self.board[y][x][0] == 'GOAL':
					sys.stdout.write('G')
				elif self.board[y][x][0] == 'BARRIER':
					sys.stdout.write('*')
				else:
					sys.stdout.write(str(self.board[y][x]))
				x+=1
			y += 1
			sys.stdout.write('\n')
			
	def isBarrier(self,position):
		if self.board[position[1]][position[0]] == 'BARRIER':
			return True
		return False
	def isGoal(self,position):
		if self.board[position[1]][position[0]] == 'GOAL':
			return True	
		return False

	def updateBoard(self,position,die):
		loc = position[1]
		self.board[position[0]].pop(position[1])
		self.board[position[0]].insert(loc, die.innerTube[1])

	def resetBoard(self,position,die,action):
		if(action == "UP"):
			position[1] -= 1 
		elif(action == "DOWN"):
			position[1] += 1
		elif(action == "RIGHT"):
			position[0] += 1
		elif(action == "LEFT"):
			position[0] -= 1
		self.board[position[0]].pop(position[1])
		self.board[position[0]].insert(position[1],"OPEN")
