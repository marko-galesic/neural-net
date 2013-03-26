import board

class Die:
	innerTube = []
	verticalTube = []
	
	def __init__(self):
		self.innerTube = [5,1,2,6]
		self.verticalTube = [3,1,4,6]

	def reverseRoll(self, direction):
		if direction == 'UP':
			self.roll('DOWN')
		elif direction == 'DOWN':
			self.roll('UP')
		elif direction == 'LEFT':
			self.roll('RIGHT')
		elif direction == 'RIGHT':
			self.roll('LEFT')
	def roll(self, direction):
		#				Down
		#				 |
		#				 \/
		#				| X |
		# Left <	| X | X | X | > Right
		#				| X |
		#				| X |
		#		  		 /\
		#		  		 |
		#		  		 Up
		# Functionally
		# Left '=' Up	
		# Down '=' Right
		print("Tubes\n" + str(self.dieInnerTube) + "\n" + str(self.dieVerticalTube))
		if ( direction == "RIGHT" ):
			self.innerTube.insert( self.innerTube.pop(), 0 )
			self.verticalTube[1] = self.innerTube[1]
		if ( direction == "LEFT" ):
			self.innerTube.append( self.innerTube.pop(0) )
			self.verticalTube[1] = self.innerTube[1]
		if ( direction == "DOWN" ):
			self.verticalTube.insert( self.verticalTube.pop(), 0 )
			self.innerTube[1] = self.verticalTube[1]
		if ( direction == "UP" ):
			self.verticalTube.append( self.verticalTube.pop(0) )
			self.innerTube[1] = self.verticalTube[1]
	def sixOnTop():
		if self.innerTube[1] == 6 or self.verticalTube[1] == 6:
			return True
		else:
			return False
