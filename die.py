import board

class Die:
	dieInnerTube = []
	dieVerticalTube = []
	
	def __init__(self):
		self.dieInnerTube = [4,1,3,6]
		self.dieVerticalTube = [2,1,5,6]
#		print(self.dieVertivalTube)

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
		print(direction)
		if ( direction == "RIGHT" ):
			self.dieInnerTube.insert( self.dieInnerTube.pop(), 0 )
			self.dieVerticalTube[1] = self.dieInnerTube[1]
		if ( direction == "LEFT" ):
			self.dieInnerTube.append( self.dieInnerTube.pop() )
			self.dieVerticalTube[1] = self.dieInnerTube[1]
		if ( direction == "DOWN" ):
			self.dieVerticalTube.insert( self.dieVerticalTube.pop(), 0 )
			self.dieInnerTube[1] = self.dieVerticalTube[1]
		if ( direction == "UP" ):
			print(self.dieVerticalTube.pop())
			print(self.dieVerticalTube)
			self.dieVerticalTube.append( self.dieInnerTube.pop() )
			print(self.dieVerticalTube)
			self.dieInnerTube[1] = self.dieVerticalTube[1]
		print("Tubes After\n" + str(self.dieInnerTube) + "\n" + str(self.dieVerticalTube))
	def sixOnTop(self):
		if self.dieInnerTube[1] == 6 or self.dieVerticalTube[1] == 6:
			return True
		else:
			return False
