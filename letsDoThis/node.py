class GameNode:
	state = None
	depth = None
	parent = None

	def __init__(self,state,depth,parent):
		self.state = state
		self.depth = depth
		self.parent = parent

	def getNewNextStates(self,puzzle,visited,numVisitedNodes,numGeneratedNodes,heuristic):
		numVisitedNodes += 1
		nextStates = []
		for neighbor in self.state.neighbors(puzzle):
			self.depth = self.depth + heuristic(neighbor) + 1
			if(neighbor not in visited or self.depth < visited[neighbor]):
				nextStates.append(GameNode(neighbor,self.depth,self))
				numGeneratedNodes += 1
		return [self.depth,numVisitedNodes,numGeneratedNodes,nextStates]

	def getPathTaken(self):
		path = []
		currentNode = self
		while currentNode != None:
			path.append([currentNode,currentNode.state.action])
			currentNode = currentNode.parent
		return path
