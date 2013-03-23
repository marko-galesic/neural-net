def roll(direction, innerTube, verticalTube):
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
		innerTube.insert( innerTube.pop(), 0 )
		verticalTube[1] = innerTube[1]
	if ( direction == "LEFT" ):
		innerTube.append( innerTube.pop() )
		verticalTube[1] = innerTube[1]
	if ( direction == "DOWN" ):
		verticalTube.insert( verticalTube.pop(), 0 )
		innerTube[1] = verticalTube[1]
	if ( direction == "UP" ):
		verticalTube.append( innerTube.pop() )
		innerTube[1] = verticalTube[1]
	