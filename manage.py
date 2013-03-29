def boardSpace(board, position):
		xCoord = position[0]
		yCoord = position[1]
		#yCoord = (position[1] - board.yRange) * -1
		#print("<> " + str(xCoord) + str(yCoord))
		return [yCoord, xCoord]
	
def playerSpace(board, position):
	xCoord = position[0]
	yCoord = (position[1] - board.yRange) * -1
	return [xCoord, yCoord]