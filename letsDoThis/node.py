class GameNode:
	state = None
	depth = None
	parent = None

	def __init__(self,state,depth,parent):
		self.state = state
		self.depth = depth
		self.parent = parent

	def getNewNextStates(self,puzzle,visited,numVisitedNodes,numGeneratedNodes,heuristic):
		visited[self.state] = self.depth
		numVisitedNodes += 1
		nextStates = []
		for neighbor in self.state.neighbors(puzzle):
			newDepth = self.depth + heuristic(neighbor) + 1
			if(neighbor not in visited or newDepth < visited[neighbor]):
				nextStates.append(GameNode(neighbor,newDepth,self))
				numGeneratedNodes += 1
		for state in nextStates:
			print(state.state.action)
		return [visited,numVisitedNodes,numGeneratedNodes,nextStates]

	def getPathTaken(self):
		path = []
		currentNode = self
		while currentNode != None:
			path.append([currentNode,currentNode.action])
			currentNode = currentNode.parent
		return path
