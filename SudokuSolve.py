#!/usr/bin/python

from math import sqrt
import copy
import sys
import time

class Solver:

	def __init__( self, sodukuFile='' ):
		self.solutions = []
		self.grid = []
		self.psbGrid = []
		if(sodukuFile!=''):
			self.grid = self.ReadGridFromFile( sodukuFile )
			self.psbGrid = self.CreatePsbGrid( self.grid )
		
	def Solve(self):
		self.FillGrid( self.grid, 0 )
		return self.solutions
		
	#File read file from grid
	def ReadGridFromFile( self, filename ):
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
	def FindPsbs( self, grid, x, y ):
		psbs = []
		
		col = self.ColToArray( grid, y )
		block = self.BlockToArray( grid, self.LocateBlock( [x, y], sqrt( len( grid ) ) ) )

		for i in range( 1, len( grid ) + 1 ):
			if i not in grid[x]:
				if i not in col:
					if i not in block:
						psbs.append( i )
		return psbs

	#Checks for duplicates within the array
	#RETURNS: False if row is valid
	def CheckArray( self, array ):
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
	def ColToArray( self, grid, colNum ):
		if colNum < len( grid ):
			array = []
			for row in grid:
				array.append( row[colNum] )
			return array

	#Validates the size of a given grid
	#Also checks if it is a 2D array
	#RETURNS: true if valid
	def CheckGridDimensions( self, grid ):
		valid = False
		
		a = sqrt( len( grid ) )

		if len( grid ) > 0 and len( grid[0] ) > 0 and a%1 == 0:
				valid = True
			
		return valid

	#Converts a block to an array
	#RETURNS: the block as an array
	def BlockToArray( self, grid, blockNum ):
		xcoord = 0
		ycoord = 0
		gridSq = int(sqrt( len( grid ) ))
		array = []
		
		ycoord = int(blockNum // gridSq) * gridSq
		xcoord = int(blockNum % gridSq) * gridSq
		
		for y in range(ycoord, ycoord+gridSq):
			for x in range(xcoord, xcoord+gridSq):
				array.append( grid[y][x] )
				
		return array

	#Returns a location for a empty value
	def LocateNextEmpty( self, grid ):
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
	def LocateBlock( self, coords, gridSq ):
		x = coords[0] // gridSq
		y = coords[1] // gridSq
		return x * gridSq + y

	def PrintGrid( self, grid ):
		linePrint = []
		for k in range( 0, len( grid ) ):
			linePrint.append( '-----' )
			
		for i in range( 0, len( grid ) ):
			#print grid[i]
			if i % sqrt( len( grid ) ) == 0:
				print ''.join( linePrint )
			self.CleanRowPrint( i, grid[i] )
		print ''.join( linePrint )
			
	def CleanRowPrint( self, rowNum, array ):
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
			
	def ValidateGrid( self, grid, x, y ):
		#Checking row
		check = self.CheckArray( grid[x] )
		
		#Checking column
		array = self.ColToArray( grid, y )
		check = check & self.CheckArray( array )
		
		#Checking block
		array = self.BlockToArray( grid, self.LocateBlock( [x, y], sqrt( len( grid ) ) ) )
		check = check & self.CheckArray( array )
		
		return check

	#Generates a grid that contains the possibilities
	#for each cell
	#RETURN: possibility grid
	def CreatePsbGrid( self, grid ):
		psb = []
		for x in range( 0, len( grid ) ):
			psb.append( [] )
			for y in range( 0, len( grid ) ):
				possibles = []
				if grid[x][y] == 0:
					possibles = self.FindPsbs( grid, x, y )
				psb[x].append( possibles )
		return psb

	#Updates the possibility grid with the new value
	def UpdatePsb( self, x, y, val ):
		#print "Updating (%d, %d) with (%d)." % (x, y, val)
		#CleanRowPrint( x, grid[x] )
		
		#cleaning out the filled cell
		if val != 0:
			self.psbGrid[x][y] = []
		for cell in self.psbGrid[x]:
			if val in cell:
				cell.remove( val )
				
		column = self.ColToArray( self.psbGrid, y )
		for cell in column:
			if val in cell:
				cell.remove( val )
		
		blockNum = self.LocateBlock( [x,y], sqrt( len( self.psbGrid ) ) )
		block = self.BlockToArray( self.psbGrid, blockNum )
		for cell in block:
			if val in cell:
				cell.remove( val )
		
		#print psbGrid

	#Recursive function to fill grid
	def FillGrid( self, grid, val ):
		nextCoord = self.LocateNextEmpty( grid )
		x = nextCoord[0]
		y = nextCoord[1]
			
		grid[x][y] = val
		undoGrid = copy.deepcopy( self.psbGrid )
		self.UpdatePsb( x, y, val )
		
		check = self.ValidateGrid( grid, x, y )
		if check == True:
			nextCoord = self.LocateNextEmpty( grid )
			nextX = nextCoord[0]
			nextY = nextCoord[1]
			if nextX == -1:
				self.solutions.append( grid )
				return True
			if len( self.psbGrid[nextX][nextY] ) > 0:
				for psb in self.psbGrid[nextX][nextY]:
					#print "%d: On the iteration %d..." % (val,i)
					check = self.FillGrid( grid, psb )
					if check == True:
						return True
		
		#Nothing worked. Undo changes and just return false
		self.psbGrid = copy.deepcopy( undoGrid )
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

def main():
	if len(sys.argv) != 2:
		sys.exit("Please specify an input file.")
	sudokuFile = sys.argv[1]
	mySolver = Solver(sudokuFile)
	start = time.clock()
	solutions = mySolver.Solve()
	end = time.clock()
	count = 0
	for item in solutions:
		count = count + 1
		print "Solution %d:" % count
		mySolver.PrintGrid( item )
	print "Solutions found in: %f seconds" % (end - start)

if __name__ == '__main__': 
	main() 
########################################
