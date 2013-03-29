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
			newDepth = self.depth + heuristic(neighbor) + 1
#			print("+")
			if(neighbor not in visited or newDepth < visited[neighbor]):
#				print("HI " + str(neighbor.action))
				nextStates.append(GameNode(neighbor,newDepth,self))
				numGeneratedNodes += 1
		return [self.depth,numVisitedNodes,numGeneratedNodes,nextStates]

	def getPathTaken(self):
		path = []
		currentNode = self
		while currentNode != None:
#			print(str(currentNode.state.action) + " => " + str([currentNode.state.x,currentNode.state.y]) + " : " + str(currentNode.state.die))		
		#while currentNode != None:
			path.append([currentNode,currentNode.state.action])
			currentNode = currentNode.parent
			#print(str(currentNode.state.action) + " => " + str([currentNode.state.x,currentNode.state.y]))
		return path
