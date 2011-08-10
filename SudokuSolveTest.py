import unittest
import SudokuSolve
from math import sqrt

########################################
#			Test Cases
########################################
class TestStuff(unittest.TestCase):
	def setUp(self):
		self.mySolver = SudokuSolve.Solver()
	
	def test_CheckArray(self):
		#print "Testing array check..."
		a = [4, 8, 9, 2, 1, 3] #should pass
		b = [8, 8, 2, 1, 3, 9] #should fail
		
		failed = True
		
		if self.mySolver.CheckArray( a ) == True:
			failed = False
		else:
			failed = True
			
		if self.mySolver.CheckArray( b ) == False:
			failed = False
		else:
			failed = True
			
		self.assertFalse(failed)

	def test_ColToArray(self):
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
		
		array = self.mySolver.ColToArray( a, 0 )
		
		if array == checkArray:
			failed = False
			
		self.assertFalse(failed)

	def test_CheckGridDimensions(self):
		#print "Testing grid validation..."
		a = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
			
		failed = True
		
		valid = self.mySolver.CheckGridDimensions( a )
		if valid == False:
			failed = False
			
		self.assertFalse(failed)
		
	def test_BlockToArray(self):
		#print "Testing blcok to array..."
		a = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
			]
		checkArray = [3, 4, 7, 8]
		
		failed = True
		
		array = self.mySolver.BlockToArray( a, 1 )
		
		if array == checkArray:
			failed = False
			
		self.assertFalse(failed)
		
	def test_LocateNextEmpty(self):
		failed = True
		a = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 0, 12],
			[13, 14, 15, 16]
			]
		val = self.mySolver.LocateNextEmpty( a )
		if val == [2,2]:
			failed = False
		self.assertFalse(failed)
		
	def test_LocateBlock(self):
		failed = True
		grid = self.mySolver.ReadGridFromFile('TestCase1.txt')
		val = self.mySolver.LocateBlock( [0,3], sqrt( len( grid ) ) )
		if val == 1:
			failed = False
		self.assertFalse(failed)
		
if __name__ == '__main__':
	unittest.main()