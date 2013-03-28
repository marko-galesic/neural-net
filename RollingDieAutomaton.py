import copy
from game import Game
from board import Board

class RollingDieAutomaton:
	game = None
	gameBoardFile = None
	DIRECTIONS 	= ['UP','DOWN','LEFT','RIGHT']	# Direction enumeration
	nextStates = []
	savedStates = []
	
	def __init__(self, aFileForTheBoard):
		self.gameBoardFile = aFileForTheBoard
		self.game = Game()
		self.game.setUpBoard(aFileForTheBoard)
	# Implementation of A*
	#def solveThePuzzle():
	
	def demo(self, depth):
		self.showGraph(self.game, depth)

	def showGraph(self, game, depth):
		if(depth > 0):
			# Draw current game states
			# CODE FOR THAT HERE #
			#game.board.resetBoard(game.position,game.die,"NONE")
			#temp = self.gameCopy(game)
			actions = self.stateActions(game.board, game.die, game.position)
			#game.board.boardDisplay()
			newActions = []
			
			print("This should return something " + str(actions))
			for action in actions:
				tempState = self.gameCopy(game)
				
				self.act(tempState,action)
				tempState.board.boardDisplay()
				newAction = [tempState.position,tempState.die]
				inAction = False
				for act in self.savedStates:
					if (act == action):
						print("A Saved State")
						inAction = True
						break
				for act in self.nextStates:
					if(act[0] == action):
						print("Already in nextStates")
						inAction = True
						break
				if (not inAction):
					#game.board.boardDisplay()
					newActions.append([newAction,copy.deepcopy(game)])
			self.nextStates.extend(newActions)
			#self.nextStates[0][1].board.boardDisplay()
			# Go through all actions
			
			nextState = self.nextStates[0]
			self.act(nextState[1], nextState[0])
			self.nextStates.pop(0)
			if self.isOnGoal(nextState[1].board, nextState[1].position):
				return True
			self.savedStates.append([nextState[1].position,nextState[1].die])
			#newState.board.resetBoard(game.position,game.die,action)
			#nextState[1].board.boardDisplay()
			self.showGraph(nextState[3], depth - 1)

	def gameCopy(self,game):
		newGame = Game()
		newBoard = Board(copy.deepcopy(game.board.board))
		newPosition = game.position[:]
		newGame.setBoard(newBoard,newPosition)
		return newGame

	def act(self,game, action):
		self.rollDie(game.die, game.position, action)
		game.board.updateBoard(game.position,game.die)
		
	# Returns whether or not the die is on a barrier on the game board
	def isOnBarrier(self,board, position):
		return board.isBarrier(self.boardSpace(board, position))
	
	def isOnGoal(self,board, position):
		return board.isGoal(self.boardSpace(board, position))

	def beenToState(self,die,position):
		for state in self.savedStates:
			if(state[0] == position and die.innerTube == state[1].innerTube and die.verticalTube == state[1].verticalTube):
				return False
		return True
		
	# Returns all actions relevant from current state (read relevant = valid)
	def stateActions(self,board, die, position):
		actions = []
		for dir in self.DIRECTIONS:
			self.rollDie(die, position, dir)
			if ((self.beenToState(die,position) and not die.sixOnTop()) and self.isInBounds(board, position) and (not self.isOnBarrier(board, position))):
				actions.append(dir)
			self.rollback(die, position, dir)
		return actions
		
	def boardSpace(self, board, position):
		xCoord = position[0]
		yCoord = position[1]
		#yCoord = (position[1] - board.yRange) * -1
		#print("<> " + str(xCoord) + str(yCoord))
		return [yCoord, xCoord]
		
	def reverse(self,position, direction):
		self.dirMovement(position, direction, True)
			
	def moveForward(self,position, direction):
		self.dirMovement(position, direction, False)
		
	def dirMovement(self, position, direction, reverse):
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
			self.positionInBoardSpace = self.boardSpace(board, position)
			spot = self.boardSpace(board, position)
			if(spot[1] < board.yRange 		and 
				spot[1] >= 0				and
				spot[0] < board.xRange 	and 
				spot[0] >= 0):
				return True
			else:
				return False

automaton = RollingDieAutomaton("Maze1.txt")
automaton.demo(2)
