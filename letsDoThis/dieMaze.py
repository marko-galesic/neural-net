import sys
import Node
import State

puzzle = []
goal = None
visited = []
nextStates = []

numVisitedNodes = 0
numGeneratedNodes = 0

heristic = lambda state: 0

def aStar(state):
	global nextStates = []
	global visited = []
	global numVisitedNodes = 1
	global numGeneratedNodes = 0
	
	if (state.x,state.y) === goal and state.die[0] == 1:
		return True
	
	nextStates.append(Node(state,0,None))
	visited[state] = 0

	foundGoal = False
	while not foundGoal:
		if (len(nextStates) == 0):
			break
		nextNode = None
		while (not nextNode or nextNode.state in visited and visited[nextNode.state] < nextNode.cost):
			nextNode = nextStates.pop(0)

		if(nextNode.x,nextNode.y) == goal and state.die[0] == 1:
			foundGoal = True
			break
		else:
			nextNode.getNewNextStates()
			
def strightLineDistance(state):
	return "Todo"

def manhattanDistance(state):
	return "Todo"

def dieTurn(state):
	return "Todo"

def results():
	for action, newState in path:
		print("%s => %s" % (action,newState))
	print("%s visited out of %s generated." % (global numVisitedNode, global numGeneratedNode))

def parse(self,maze):
	board = []
	startState = None
	goalState = None
	mazeBoard = open(maze,'r')
	int x = 0
	for line in mazeBoard:
		loc = 0
		column = []
		while loc < len(line):
			s = line[loc]
			if (s == "S"):
				s = "START"
				startState = State(x,loc,(1,2,3),None)
			elif(s == "G"):
				s = "GOAL"
				goalState = [x,loc]
			elif(s == "."):
				s = "OPEN"
			elif(s =="*"):
				s = "BARRIOR"
			if(s != "\n"):
				column.append([s,[]])
			loc += 1
		board.append(column)
		x+=1
	return [board,startState,goalState]

def main():
	puzzle = parse(argc[1],'r')
	board = puzzle[0]
	startState = puzzle[1]
	global goal = puzzle[2]
	print("Straight Line Distance")
	heuristic = strightLineDistance
	results()
	print("Manhattan Distance")
	heuristic = manhattan_distance
	results()
	print("Die Turn")
	heuristic = dieTurn
	presults()