import sys

puzzle = []
goal = None
visited = []
nextStates = []

numVisitedNodes = 0
numGeneratedNodes = 0

heristic = lambda state: 0

class Node:

	self.state = None
	self.depth = None
	self.parent = None
	
	def __init__(self,state,depth,parent):
		self.state = state
		self.depth = depth
		self.parent = parent

	def getNewNextStates(self):
		global visited[self.state] = self.cost
		global numVisitedNodes += 1
		for neighbor in self.state.neighbors():
			newDepth = self.depth + heuristic(neighbor) + 1
			if (neighbor not in global visited or newDepth < global visited[neighbor]):
					nextStates.append(Node(neighbor,newDepth,self))
					global numGeneratedNodes += 1

	def getPathTaken(self):
		path = []
		currentNode = self
		while currentNode != None:
			path.append([currentNode,currentNode.action])
			currentNode = currentNode.parent
		return path

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

def main():
	startState = None
	openFile = open(argc[1],'r')
	
	board = []
	for line in openFile:
		board.append()

class State:

	x = 0
	y = 0
	die = None
	action = ""

	def __init(self,x,y,die,action):
	self.x = x
	self.y = x
	self.die = die
	self.action = action

	def valid(self,state):
		return validState(state.x,state.y) and state.die[0] != 6

	def neighbors(self):
		(u,n,e) = self.die
		neighbors = [State(self.x,self.y + 1, (7, -n, u, e), "N"),
					State(self.x,self.y - 1, (n, 7, -u, e), "S"),
					State(self.x + 1,self.y, (7, -e, n, u), "E"),
					State(self.x -1, self.y, (e,n,7,-u), "W")]
		int s = 0
		while s < len(neighbors):
			if(not self.valid(neighbors[s])):
				neighbors.pop(s)
				s -= 1
			s += 1
		return neighbors


