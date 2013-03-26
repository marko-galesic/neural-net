import board

class Die:
	dieInnerTube = []
	dieVerticalTube = []
	
	def __init__(self):
		print("need to init die")

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
			self.dieVerticalTube.append( self.dieInnerTube.pop() )
			self.dieInnerTube[1] = self.dieVerticalTube[1]
	def sixOnTop():
		if self.innerTube[1] == 6 or self.verticalTube[1] == 6:
			return True
		else:
			return False
