def displayDie(orientation):
	innerTube
	if orientation == "default":
		North 	= '2'
		West 	= '4'
		East	= '3'
		South	= '5'
		OnTop	= '1'
		Bottom	= '6'
	if orientation == "90CC":
		North 	= '4'
		West 	= '5'
		East	= '2'
		South	= '3'
		Center	= '1'
		Bottom	= '6'
	if orientation == "180CC":
		North 	= '5'
		West 	= '3'
		East	= '4'
		South	= '2'
		OnTop	= '1'
		Bottom	= '6'
	if orientation == "90CW":
		North 	= '3'
		West 	= '2'
		East	= '5'
		South	= '4'
		Center	= '1'
		Bottom	= '6'
	
	print '    ' + North
	print West + '   ' + OnTop + '   ' + East
	print '    ' + South
	print '    ' + Bottom
	
displayDie("default")
displayDie("90CC")
displayDie("180CC")
displayDie("90CW")