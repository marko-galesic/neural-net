import copy
import game

class RollingDieAutomaton:
	game 			= None
	gameBoardFile 	= None
	DIRECTIONS 	= ['UP','DOWN','LEFT','RIGHT']	# Direction enumeration
	
	def __init__(self, aFileForTheBoard):
		gameBoardFile = aFileForTheBoard
		game = Game(gameBoardFile)
		
	# Implementation of A*
	#def solveThePuzzle():
	
	def demo(depth):
		gameDemo = Game(gameBoardFile)
		
		showGraph(gameDemo, depth)
	def showGraph(game, depth):
		# Draw current game state
		# CODE FOR THAT HERE #
		actions = stateActions(game.board, game.die, game.position)
		
		# Go through all actions
		for action in actions:
			newState = copy.deepcopy(game)
			act(newState, action)
			if isOnGoal(newState.board, newstate.position):
				return
			showGraph(newState, depth - 1)
		
	def act(game, action):
		rollDie(game.die, game.position, action)
		
	# Returns whether or not the die is on a barrier on the game board
	def isOnBarrier(board, position):
		return board.isBarrier(boardSpace(position))
	
	def isOnGoal(board, position)
		return board.isGoal(boardSpace(position))
		
	# Returns all actions relevant from current state (read relevant = valid)
	def stateActions(board, die, position):
		actions = []
		for dir in DIRECTIONS:
			rollDie(die, position, dir)
			if not (die.sixOnTop() or isInBounds(board, position) or isOnBarrier(board, position)):
				actions.append(dir)
			rollback(die, position, dir)
	def boardSpace(position):
		xCoord = position[0]
		yCoord = ( position[1] - yRange ) * -1
		return [yCoord, xCoord]
		
	def reverse(position, direction):
		dirMovement(position, direction, True)
			
	def moveForward(position, direction):
		dirMovement(position, direction, False)
		
	def dirMovement(position, direction, reverse):
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
	
	def rollDie(die, position, direction):
		# Modify die state
		die.roll(direction)
		
		# Change game state
		moveForward(position, direction)
	def rollback(die, position, direction):
		# Modify die state
		die.reverseRoll(direction)
		
		# Change game state
		reverse(position, direction)
		
	# Checks whether die position is in board space
	# Returns false if bound check fails
	def isInBounds(board, position):
			positionInBoardSpace = boardSpace(position)
			if 	positionInBoardSpace[0] <= board.yRange 	and 
				positionInBoardSpace[0] >= 0				and
				positionInBoardSpace[1] <= board.xRange 	and 
				positionInBoardSpace[1] >= 0				and
				return True
			else:
				return False

RollingDieAutomaton automaton = RollingDieAutomaton(file)
automaton.demo(10)