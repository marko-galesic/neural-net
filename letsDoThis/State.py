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