#!/usr/bin/python

from math import sqrt
import copy
import sys
import time

#File read file from grid
def ReadGridFromFile( filename ):
	f = open(filename,'r')
	grid = []
	currRow = 0
	for line in f:
		grid.append( [] )
		values = line.split( ' ' )
		for val in values:
			if val != '\n':
				valInt = int( val )
				grid[currRow].append( valInt )
		currRow = currRow + 1
	return grid
	
#Checks a grid at certain coordinates and list its possibile values
#RETURNS: list of possible values for coords
def FindPsbs( grid, x, y ):
	psbs = []
	
	col = ColToArray( grid, y )
	block = BlockToArray( grid, LocateBlock( [x, y], sqrt( len( grid ) ) ) )

	for i in range( 1, len( grid ) + 1 ):
		if i not in grid[x]:
			if i not in col:
				if i not in block:
					psbs.append( i )
	return psbs

#Checks for duplicates within the array
#RETURNS: False if row is valid
def CheckArray( array ):
	newArray = copy.deepcopy( array )
	newArray.sort()
	currVal = 0
	valid = True
	for val in newArray:
		if val != 0:
			if val == currVal:
				valid = False
			else:
				currVal = val
	return valid

#Converts a specified column to an array
#RETURNS: the column in array format
def ColToArray( grid, colNum ):
	if colNum < len( grid ):
		array = []
		for row in grid:
			array.append( row[colNum] )
		return array

#Validates the size of a given grid
#Also checks if it is a 2D array
#RETURNS: true if valid
def CheckGridDimensions( grid ):
	valid = False
	
	a = sqrt( len( grid ) )
	
	if len( grid ) > 0 and len( grid[0] ) > 0:
		if a%1 == 0:
			valid = True
	else:
		valid = False
		
	return valid

#Converts a block to an array
#RETURNS: the block as an array
def BlockToArray( grid, blockNum ):
	xcoord = 0
	ycoord = 0
	gridSq = int(sqrt( len( grid ) ))
	array = []
	
	ycoord = int(blockNum // gridSq) * gridSq
	xcoord = int(blockNum % gridSq) * gridSq
	for y in range(ycoord, xcoord+gridSq):
		for x in range(xcoord, ycoord+gridSq):
			array.append( grid[y][x] )
			
	return array

#Returns a location for a empty value
def LocateNextEmpty( grid ):
	x = 0
	y = 0
	for row in grid:
		for val in row:
			if val == 0:
				return [x,y]
			y = y + 1
		x = x + 1
		y = 0
	return [-1,0]

#Calculates the block belonging to the coords
def LocateBlock( coords, gridSq ):
	x = coords[0] // gridSq
	y = coords[1] // gridSq
	return x * gridSq + y
	
########################################
#			Test Cases
########################################
def TestCheckArray():
	#print "Testing array check..."
	a = [4, 8, 9, 2, 1, 3] #should pass
	b = [8, 8, 2, 1, 3, 9] #should fail
	
	failed = True
	
	if CheckArray( a ) == True:
		failed = False
	else:
		failed = True
		
	if CheckArray( b ) == False:
		failed = False
	else:
		failed = True
		
	return failed

def TestColToArray():
	#print "Testing column to array..."
	a = [
		[1, 2, 3, 4, 5],
		[6, 7, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20],
		[21, 22, 23, 24, 25]
		]
	checkArray = [1, 6, 11, 16, 21]
	
	failed = True
	
	array = ColToArray( a, 0 )
	
	if array == checkArray:
		failed = False
		
	return failed

def TestCheckGridDimensions():
	#print "Testing grid validation..."
	a = [
		[1, 2, 3, 4, 5],
		[6, 7, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20],
		[21, 22, 23, 24, 25]
		]
		
	failed = True
	
	valid = CheckGridDimensions( a )
	if valid == False:
		failed = False
		
	return failed
	
def TestBlockToArray():
	#print "Testing blcok to array..."
	a = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
		]
	checkArray = [3, 4, 7, 8]
	
	failed = True
	
	array = BlockToArray( a, 1 )
	
	if array == checkArray:
		failed = False
		
	return failed
	
def TestLocateNextEmpty():
	failed = True
	a = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 0, 12],
		[13, 14, 15, 16]
		]
	val = LocateNextEmpty( a )
	if val == [2,2]:
		failed = False
	return failed
	
def TestLocateBlock():
	failed = True
	grid = ReadGridFromFile('TestCase1.txt')
	val = LocateBlock( [0,3], sqrt( len( grid ) ) )
	if val == 1:
		failed = False
	return failed
	
def FailedString( failed ):
	if failed:
		return "!!!! Failed !!!!"
	else:
		return "Passed"
		
def BigTest():
	testResults = []
	testResults.append( TestCheckArray() )
	testResults.append( TestColToArray() )
	testResults.append( TestCheckGridDimensions() )
	testResults.append( TestBlockToArray() )
	testResults.append( TestLocateNextEmpty() )
	testResults.append( TestLocateBlock() )
	
	a = 0
	for test in testResults:
		print "Test %d: %s" % (a, FailedString( test ))
		a = a + 1
########################################

def PrintGrid( grid ):
	linePrint = []
	for k in range( 0, len( grid ) ):
		linePrint.append( '-----' )
		
	for i in range( 0, len( grid ) ):
		#print grid[i]
		if i % sqrt( len( grid ) ) == 0:
			print ''.join( linePrint )
		CleanRowPrint( i, grid[i] )
	print ''.join( linePrint )
		
def CleanRowPrint( rowNum, array ):
	cleanPrint = []
	for i in range( 0, len( array ) ):
		if i % sqrt( len( array ) ) == 0:
			cleanPrint.append( "| " )
		val = array[i]
		if val > 9:
			cleanPrint.append( str( val ) )
		else:
			cleanPrint.append( str( val ) )
			cleanPrint.append( ' ' )
	cleanPrint.append( "| " )
	#print "%d: [ %s ]" % (rowNum, ' '.join( cleanPrint ) )
	print ' '.join( cleanPrint )
		
def ValidateGrid( grid, x, y ):
	#Checking row
	check = CheckArray( grid[x] )
	
	#Checking column
	array = ColToArray( grid, y )
	check = check & CheckArray( array )
	
	#Checking block
	array = BlockToArray( grid, LocateBlock( [x, y], sqrt( len( grid ) ) ) )
	check = check & CheckArray( array )
	
	return check

#Generates a grid that contains the possibilities
#for each cell
#RETURN: possibility grid
def CreatePsbGrid( grid ):
	psb = []
	for x in range( 0, len( grid ) ):
		psb.append( [] )
		for y in range( 0, len( grid ) ):
			possibles = []
			if grid[x][y] == 0:
				possibles = FindPsbs( grid, x, y )
			psb[x].append( possibles )
	return psb

psbGrid = []
solutions = []

#Updates the possibility grid with the new value
def UpdatePsb( x, y, val ):
	global psbGrid
	
	#print "Updating (%d, %d) with (%d)." % (x, y, val)
	#CleanRowPrint( x, grid[x] )
	
	#cleaning out the filled cell
	if val != 0:
		psbGrid[x][y] = []
	for cell in psbGrid[x]:
		if val in cell:
			cell.remove( val )
			
	column = ColToArray( psbGrid, y )
	for cell in column:
		if val in cell:
			cell.remove( val )
	
	blockNum = LocateBlock( [x,y], sqrt( len( psbGrid ) ) )
	block = BlockToArray( psbGrid, blockNum )
	for cell in block:
		if val in cell:
			cell.remove( val )
	
	#print psbGrid

#Recursive function to fill grid
def FillGrid( grid, val ):
	global psbGrid
	
	nextCoord = LocateNextEmpty( grid )
	x = nextCoord[0]
	y = nextCoord[1]
		
	grid[x][y] = val
	undoGrid = copy.deepcopy( psbGrid )
	UpdatePsb( x, y, val )
	
	check = ValidateGrid( grid, x, y )
	if check == True:
		nextCoord = LocateNextEmpty( grid )
		nextX = nextCoord[0]
		nextY = nextCoord[1]
		if nextX == -1:
			global solutions
			solutions.append( grid )
			return True
		if len( psbGrid[nextX][nextY] ) > 0:
			for psb in psbGrid[nextX][nextY]:
				#print "%d: On the iteration %d..." % (val,i)
				check = FillGrid( grid, psb )
				if check == True:
					return True
	
	#Nothing worked. Undo changes and just return false
	psbGrid = copy.deepcopy( undoGrid )
	grid[x][y] = 0
	return False
	
#Find the most common value and choose to solve that next
#Add pointers to the end of each row/col to maintain stacks of values possible
#	Each time you add a value to the row/col, remove from stack
#	Each time you remove a value from row/col, add back to the stack
#
#Add a stack per cell for possible values
#	Same concepts as above apply but on a per cell basis
#	Uses up way more memory, but should be faster for larger solutions
#	Could also apply logic to these stacks
#		Ex: block contains 2 cells in the same row/col that contain same value
#		Remove other values in the same row/col
#
#Only add value if the stack size is 1, otherwise move on
#TODO: Sort the lengths of arrays in psbGrid and select the next cell based on the shortest length found.
########################################
#				MAIN
########################################
#BigTest()
grid = ReadGridFromFile(sys.argv[1])
psbGrid = CreatePsbGrid( grid )
start = time.clock()
FillGrid( grid, 0 )
end = time.clock()
count = 0
for item in solutions:
	count = count + 1
	print "Solution %d:" % count
	PrintGrid( item )
print "Solutions found in: %f seconds" % (end - start)
########################################
