from sys import argv
import sys
from node import GameNode
from state import State
import math
import copy

puzzle = []
goal = None
visited = {}
nextStates = []

numVisitedNodes = 0
numGeneratedNodes = 0

nV = 0

heristic = lambda state: 0

def aStar(state):
	global puzzle, nextStates, visited, numVisitedNoes, numGeneratedNodes, heuristic, nV
	nextStates = []
	visited = {}
	numVisitedNodes = 1
	numGeneratedNodes = 0
	
	if (state.x,state.y) == goal and state.die[1] == 1:
		return True
	
	nextStates.append(GameNode(state,0,None))

	foundGoal = False
	n = 0
	while not foundGoal:
		if (len(nextStates) == 0):
			print("break")
			break
		nextNode = nextStates.pop(0)
		notValid = haveVisited(nextNode.state,visited)
		while (notValid):
			if(len(nextStates) == 0 ):
				print("No More States")
				return False
			nextNode = nextStates.pop(0)
			numVisitedNodes += 1
#			print(numVisitedNodes)
			notValid = haveVisited(nextNode.state,visited)
		#print("-+ " + str(puzzle[nextNode.state.x][nextNode.state.y]) + "<=>" + str(state.die))
		#print(puzzle[nextNode.state.x][nextNode.state.y] == "G")
		if( puzzle[nextNode.state.x][nextNode.state.y] == "G" and state.die[0][1] == 1):
			foundGoal = True
			nV = numVisitedNodes + 0
			print("win")
			return nextNode.getPathTaken()
		else:
			nextNode.getPathTaken()
			ret = nextNode.getNewNextStates(puzzle,visited,numVisitedNodes,numGeneratedNodes,heuristic)
			visit = ret[0]
			visited[nextNode.state] = visit
			numVisitedNodes = ret[1]
			numGeneratedNodes = ret[2]
			#print("_-_-_-_-_-_-")
			#print(len(ret[3]))
			#print(len(nextStates))
			nextStates.extend(ret[3])
			
			#i = 0
			#while i < len(nextStates):
			#	j = 0
			#	while j < len(nextStates):
			#		if(not i == j):
			#			if(not (nextStates[i].state.x == nextStates[j].state.x and
			#				nextStates[i].state.y == nextStates[j].state.y and
			#				nextStates[i].state.action == nextStates[j].state.action)):
			#					nextStates.pop(j)
			#					j-=1
			#		j+=1
			#	i+=1
			n+=1
			#print(len(nextStates))
#			if (n > 10001):
#				print(len(nextStates))
#				foundGoal = True
#				return nextNode.getPathTaken()

def haveVisited(state,visited):
	for key in visited.keys():
		#print("Have Visited")
		#print([key.die,key.x,key.y])
		#print("Current Visit")
		#print([state.die,state.x,state.y])
		if ((key.die == state.die) and 
			(key.x == state.x) and
			(key.y == state.y)):	
			return True
	#print("False")
	return False

def strightLineDistance(state):
	global goal
	x = (state.x - goal[0])
	y = (state.y - goal[1])
	dist = math.sqrt(abs(x*x + y*y))
	return dist

def manhattanDistance(state):
	return abs((state.x - goal[0])) + abs((state.y - goal[1]))

def dieTurn(state):
	if(state.die[0][1] == 1):
		return 1
	return 0

def results(startState):
	global numGeneratedNodes
	path = aStar(startState)
	global nV
	if(not path == False):
		for newState, action in path:
			print("%s => [%s,%s]" % (action,newState.state.x,newState.state.y))
		print("%s visited out of %s generated." % (nV, numGeneratedNodes))

def parse(maze):
	board = []
	startState = None
	goalState = None
	mazeBoard = open(maze,'r')
	x = 0
	for line in mazeBoard:
		loc = 0
		column = []
		while loc < len(line):
			s = line[loc]
			if (s == "S"):
				startState = State(x,loc,[[2,1,5,6],[4,1,3,6]],None)
			elif(s == "G"):
				goalState = [x,loc]
			if(s != "\n"):
				column.append(s)
			loc += 1
		board.append(column)
		x+=1
	return [board,startState,goalState]

def main():
	global goal, puzzle, heuristic
	board = parse(argv[1])
	puzzle = board[0]
	startState = board[1]
	goal = board[2]
	startLine = copy.deepcopy(startState)
	startBloc = copy.deepcopy(startState)
	startFlip = copy.deepcopy(startState)
	print("Straight Line Distance")
	heuristic = strightLineDistance
	results(startLine)
	print("Manhattan Distance")
	heuristic = manhattanDistance
	results(startBloc)
	print("Die Turn")
	heuristic = dieTurn
	results(startFlip)

if __name__ == "__main__":
	main()
