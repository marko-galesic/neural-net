from sys import argv
import sys
from node import GameNode
from state import State
import math

puzzle = []
goal = None
visited = {}
nextStates = []

numVisitedNodes = 0
numGeneratedNodes = 0

heristic = lambda state: 0

def aStar(state):
	global puzzle, nextStates, visited, numVisitedNoes, numGeneratedNodes, heuristic
	nextStates = []
	visited = {}
	numVisitedNodes = 1
	numGeneratedNodes = 0
	
	if (state.x,state.y) == goal and state.die[1] == 1:
		print("at goal state")
		return True
	
	nextStates.append(GameNode(state,0,None))

	visited[state] = 0

	foundGoal = False
	while not foundGoal:
		if (len(nextStates) == 0):
			print("No new States")
			break
		nextNode = None
		while (not nextNode or nextNode.state in visited and visited[nextNode.state] < nextNode.depth):
			nextNode = nextStates.pop(0)
		print("Here?")
		if(nextNode.state.x,nextNode.state.y) == goal and state.die[1] == 1:
			foundGoal = True
			return nextNode.unwind()
		else:
			ret = nextNode.getNewNextStates(puzzle,visited,numVisitedNodes,numGeneratedNodes,heuristic)
			visited = ret[0]
			numVisitedNodes = ret[1]
			numGeneratedNodes = ret[2]
			nextStates.extend(ret[3])		
def strightLineDistance(state):
	global goal
	x = (state.x - goal[0])
	y = (state.y - goal[1])
	dist = math.sqrt(abs(x*x + y*y))
	print(dist)
	return dist

def manhattanDistance(state):
	return "Todo"

def dieTurn(state):
	return "Todo"

def results(startState):
	global numVisitedNode, numGeneratedNode
	path = aStar(startState)
	print(path)
	for action, newState in path:
		print("%s => %s" % (action,newState))
	print("%s visited out of %s generated." % (numVisitedNode, numGeneratedNode))

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
				s = "START"
				startState = State(x,loc,[[2,1,5,6],[4,1,3,6]],None)
			elif(s == "G"):
				s = "GOAL"
				goalState = [x,loc]
			elif(s == "."):
				s = "OPEN"
			elif(s =="*"):
				s = "BARRIOR"
			if(s != "\n"):
				column.append(s)
			loc += 1
		board.append(column)
		x+=1
	return [board,startState,goalState]

def main():
	global goal, puzzle, heuristic
	print("Starting maze")
	print(argv[1])
	board = parse(argv[1])
	puzzle = board[0]
	startState = board[1]
	goal = board[2]
	print("Straight Line Distance")
	heuristic = strightLineDistance
	results(startState)
	print("Manhattan Distance")
	heuristic = manhattan_distance
	results(startState)
	print("Die Turn")
	heuristic = dieTurn
	presults(stateState)

if __name__ == "__main__":
	main()
