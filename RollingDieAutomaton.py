import copy
from game import Game

class RollingDieAutomaton:
	game = None
	gameBoardFile = None
	DIRECTIONS 	= ['UP','DOWN','LEFT','RIGHT']	# Direction enumeration
	
	def __init__(self, aFileForTheBoard):
		self.gameBoardFile = aFileForTheBoard
		game = Game(self.gameBoardFile)
		
	# Implementation of A*
	#def solveThePuzzle():
	
	def demo(self, depth):
		gameDemo = Game(self.gameBoardFile)
		
		self.showGraph(gameDemo, depth)

	def showGraph(self, game, depth):
		# Draw current game states
		# CODE FOR THAT HERE #
		actions = self.stateActions(game.board, game.die, game.position)
		print("this : " + str(actions))
		# Go through all actions
		for action in actions:
			newState = copy.deepcopy(game)
			self.act(newState, action)
			if self.isOnGoal(newState.board, newstate.position):
				return
			self.showGraph(newState, depth - 1)
		
	def act(self,game, action):
		self.rollDie(game.die, game.position, action)
		
	# Returns whether or not the die is on a barrier on the game board
	def isOnBarrier(self,board, position):
		return board.isBarrier(self.boardSpace(position))
	
	def isOnGoal(self,board, position):
		return board.isGoal(boardSpace(position))
		
	# Returns all actions relevant from current state (read relevant = valid)
	def stateActions(self,board, die, position):
		actions = []
		for dir in self.DIRECTIONS:
			self.rollDie(die, position, dir)
			if not (die.sixOnTop() or self.isNotInBounds(board, position) or self.isOnBarrier(board, position)):
				actions.append(dir)
			self.rollback(die, position, dir)
		return actions
	def boardSpace(self,position):
		xCoord = position[0]
		yCoord = position[1]
		return [yCoord, xCoord]
		
	def reverse(self,position, direction):
		self.dirMovement(position, direction, True)
			
	def moveForward(self,position, direction):
		self.dirMovement(position, direction, False)
		
	def dirMovement(self,position, direction, reverse):
		print(position)
		if direction == 'UP':
			if reverse: position[1] += 1
			else: 		position[1] -= 1
		elif direction == 'DOWN':
			if reverse:	position[1] -= 1
			else: 		position[1] += 1
		elif direction == 'LEFT':
			if reverse: position[0] += 1
			else:		position[0] -= 1
		elif direction == 'RIGHT':
			if reverse: position[0] -= 1
			else:		position[0] += 1
	
	def rollDie(self,die, position, direction):
		# Modify die state
		die.roll(direction)
		
		# Change game state
		self.moveForward(position, direction)

	def rollback(self,die, position, direction):
		# Modify die state
		die.reverseRoll(direction)
		
		# Change game state
		self.reverse(position, direction)
		
	# Checks whether die position is in board space
	# Returns false if bound check fails
	def isNotInBounds(self,board, position):
			self.positionInBoardSpace = self.boardSpace(position)
			if 	(self.positionInBoardSpace[0] <= board.yRange 	and 
				self.positionInBoardSpace[0] >= 0				and
				self.positionInBoardSpace[1] <= board.xRange 	and 
				self.positionInBoardSpace[1] >= 0):
				return False
			else:
				return True

automaton = RollingDieAutomaton("Maze1.txt")
automaton.demo(10)
