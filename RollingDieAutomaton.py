import copy
from manage import *
from game import Game
from board import Board


class RollingDieAutomaton:
	game = None
	DIRECTIONS 	= ['UP','DOWN','LEFT','RIGHT']	# Direction enumeration
	nextStates = []

	def __init__(self, aFileForTheBoard):
		self.gameBoardFile = aFileForTheBoard
		self.game = Game()
		self.game.setUpBoard(aFileForTheBoard)

	# Implementation of A*
	#def solveThePuzzle():
	
	def demo(self, depth):
		self.showGraph(self.game, depth)

	def showGraph(self, game, depth):
		if(self.isOnGoal(game.board,game.position)):
			return True
		if(depth < 3):
			# Draw current game states
			# CODE FOR THAT HERE #
			actions = self.stateActions(game.board, game.die, game.position)
			#game.board.boardDisplay()
			newActions = []
			
			print("This should return something " + str(actions))
			for action in actions:
				tempState = self.gameCopy(game)
				
				self.act(tempState,action,depth)
				
				inAction = False
				
				if (not inAction):
					tempState.board.boardDisplay()
					newActions.append(tempState)
			self.nextStates.extend(newActions)
			#self.nextStates[0][1].board.boardDisplay()
			# Go through all actions
			
			#nextState = self.nextStates[0]
			#self.act(nextState[1], nextState[0])
			#self.nextStates.pop(0)
			#if self.isOnGoal(nextState[1].board, nextState[1].position):
			#	return True
			#newState.board.resetBoard(game.position,game.die,action)
			#nextState[1].board.boardDisplay()
			nextState = self.nextStates[0]
			self.nextStates.pop(0)
			self.showGraph(nextState, depth + 1)

	def gameCopy(self,game):
		newGame = Game()
		board = game.board
		newBoard = Board(copy.deepcopy(board.board))
		x = board.xRange
		y = board.yRange
		newBoard.setRange(x,y)
		loc = game.position[0][:]
		depth = game.position[1]
		newPosition = [loc,depth]
		newGame.setBoard(newBoard,newPosition)
		return newGame

	def act(self,game, action,depth):
		self.rollDie(game.die, game.position, action)
		game.board.updateBoard(game.position,game.die,depth)
		
	# Returns whether or not the die is on a barrier on the game board
	def isOnBarrier(self,board, position):
		return board.isBarrier(boardSpace(board, position[0]))
	
	def isOnGoal(self,board, position):
		return board.isGoal(boardSpace(board, position[0]))

	def beenTo(self,board,die,position):
		if(self.isInBounds(board,position)):
			
		for state in board.board[position[0][0]][position[0][1]][1]:
			if (state[1][0] == die and state[1][1] > position[1]):
				return True
		return False
		
	# Returns all actions relevant from current state (read relevant = valid)
	def stateActions(self,board, die, position):
		actions = []
		for di in self.DIRECTIONS:
			self.rollDie(die, position, di)
			if ((not self.beenTo(board,die,position)) and (not die.sixOnTop()) and self.isInBounds(board, position) and (not self.isOnBarrier(board, position))):
				actions.append(di)
			self.rollback(die, position, di)
		return actions
		
	def reverse(self,position, direction):
		self.dirMovement(position, direction, True)
			
	def moveForward(self,position, direction):
		self.dirMovement(position, direction, False)
		
	def dirMovement(self, position, direction, reverse):
		position = position[0]
		if direction == 'UP':
			if reverse: position[1] += 1
			else:		position[1] -= 1
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
	def isInBounds(self, board, position):
			self.positionInBoardSpace = boardSpace(board, position[0])
			spot = boardSpace(board, position[0])
			if(spot[1] < board.yRange 		and 
				spot[1] >= 0				and
				spot[0] < board.xRange 	and 
				spot[0] >= 0):
				return True
			else:
				return False

automaton = RollingDieAutomaton("Maze1.txt")
automaton.demo(0)
