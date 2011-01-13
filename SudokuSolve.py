#!/usr/bin/python

from math import sqrt
import copy
import sys

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
	gridSq = sqrt( len( grid ) )
	array = []
	
	ycoord = blockNum // gridSq * gridSq
	xcoord = (blockNum % gridSq) * gridSq
	
	for y in range(ycoord, ycoord+gridSq):
		for x in range(xcoord, xcoord+gridSq):
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
	grid = ReadGridFromFile('TestCase1.txt')
	val = LocateNextEmpty( grid )
	if val == [1,0]:
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
	for row in grid:
		print row
		
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

solutions = []

#Recursive function to fill grid
def FillGrid( grid, val ):
	nextCoord = LocateNextEmpty( grid )
	x = nextCoord[0]
	y = nextCoord[1]
	
	#Base cases
	if x == -1:
		global solutions
		solutions.append( grid )
		return True
		
	grid[x][y] = val
	
	print "Attempting to add: %d" % val
	PrintGrid( grid )
	
	check = ValidateGrid( grid, x, y )
	if check == True:
		for i in range( 1, len( grid ) + 1 ):
			#print "%d: On the iteration %d..." % (val,i)
			check = FillGrid( grid, i )
			if check == True:
				return True
	
	#Nothing worked, just return false
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
########################################
#				MAIN
########################################
BigTest()
grid = ReadGridFromFile(sys.argv[1])
FillGrid( grid, 0 )
count = 0
for item in solutions:
	count = count + 1
	print "Solution %d:" % count
	PrintGrid( item )
########################################