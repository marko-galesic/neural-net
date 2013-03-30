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

#Runs a*
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
	#runs to a path is found
	while not foundGoal:
		if (len(nextStates) == 0):
			break
		nextNode = nextStates.pop(0)
		notValid = haveVisited(nextNode.state,visited)

		# finds the next valid node
		while (notValid):
			if(len(nextStates) == 0 ):
				print("No More States")
				print("Visited " + str(len(visited)) + " generated " + str(numGeneratedNodes))
				return False
			smallestS = None
			smallestI = None
			s = 0
			
			#finds smallest depth
			while len(nextStates) >s:
				if(smallestS == None):
					smallestS = nextStates[s].depth
					smallestI = s
				elif(nextStates[s].depth < smallestS):
					smallestS = nextStates[s].depth
					smallestI = s
				s+=1
			nextNode = nextStates.pop(smallestI)
			numVisitedNodes += 1

			notValid = haveVisited(nextNode.state,visited)
		
		#checks if at goal state
		if( puzzle[nextNode.state.x][nextNode.state.y] == "G" and state.die[0][1] == 1):
			foundGoal = True
			nV = numVisitedNodes + 0
#			print("win")
			return nextNode.getPathTaken()
		else:
			nextNode.getPathTaken()
			
			#gets child states of the current state
			ret = nextNode.getNewNextStates(puzzle,visited,numVisitedNodes,numGeneratedNodes,heuristic)
			visit = ret[0]
			visited[nextNode.state] = visit
			numVisitedNodes = ret[1]
			numGeneratedNodes = ret[2]
			
			nextStates.extend(ret[3])
			n+=1

#Finds out if the node has been visited before
def haveVisited(state,visited):
	for key in visited.keys():
		if ((key.die == state.die) and 
			(key.x == state.x) and
			(key.y == state.y)):	
			return True
	return False

#Get the stright line distance
def strightLineDistance(state):
	global goal
	x = (state.x - goal[0])
	y = (state.y - goal[1])
	dist = math.sqrt(abs(x*x + y*y))
	return dist

#Gets the manhattan distance
def manhattanDistance(state):
	return abs((state.x - goal[0])) + abs((state.y - goal[1]))

seen = []

#Gets the Breadth First distance
def getDistancesBreathFirst(state):
	#print("Starting breath first")
	global puzzle,seen
	seen = []
	
	depth =  breathFirst([[state.x,state.y],0],state.neighbors(puzzle))
#	print("breath depth " + str(depth))
	return depth

#recursive breadth first call
def breathFirst(state,neighbors):
	global puzzle, seen
	if (state[0] == goal):
		return state[1]
	
	for stateSeen in seen:
		x = 0
		while x < len(neighbors):
			if(stateSeen[0] == [neighbors[x].x,neighbors[x].y]):
				neighbors.pop(x)
				x -= 1
			x+=1
	seen.append(state)
	for child in neighbors:
		return breathFirst([[child.x,child.y],state[1] + 1],child.neighbors(puzzle))
	return 0

#Finds is location is valid
def unSeen(v,distance):
	x,y = v
	return not valid(x,y) and type(distance[x][y]) == int

#checks if on the board or on a block
def valid(x,y):
	global puzzle
	if(not 0<=x<len(puzzle)):
		return False
	if(not 0<=y<len(puzzle[0])):
		return False
	if(puzzle[x][y] == "*"):
		return False
	return True

#filters seen
def nextStatesFilter(x,y):
	return filter(unSeen,[(x+1,y),(x-1,y),(x,y+1),(x,y-1)])

#prints the results
def results(startState):
	global numGeneratedNodes
	path = aStar(startState)
	global nV
	if(not path == False):
		for newState, action in path:
			print("%s => [%s,%s]" % (action,newState.state.x,newState.state.y))
		print("%s visited out of %s generated." % (nV, numGeneratedNodes))

#parses the board
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

#runs the program
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
	heuristic = getDistancesBreathFirst
	results(startFlip)

if __name__ == "__main__":
	main()
