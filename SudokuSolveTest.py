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
		
		self.assertTrue( self.mySolver.CheckArray( a ) )
		self.assertFalse( self.mySolver.CheckArray( b ) )

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
		
		array = self.mySolver.ColToArray( a, 0 )
			
		self.assertTrue(array == checkArray)

	def test_CheckGridDimensions(self):
		#print "Testing grid validation..."
		a = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
			
		self.assertFalse( self.mySolver.CheckGridDimensions( a ) )
		
	def test_BlockToArray(self):
		#print "Testing blcok to array..."
		a = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
			]
		checkArray = [3, 4, 7, 8]
		
		array = self.mySolver.BlockToArray( a, 1 )

		self.assertTrue(array == checkArray)
		
	def test_LocateNextEmpty(self):
		failed = True
		a = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 0, 12],
			[13, 14, 15, 16]
			]
		val = self.mySolver.LocateNextEmpty( a )

		self.assertTrue( val == [2,2] )
		
	def test_LocateBlock(self):
		failed = True
		grid = self.mySolver.ReadGridFromFile('TestCase1.txt')
		val = self.mySolver.LocateBlock( [0,3], sqrt( len( grid ) ) )

		self.assertTrue( val == 1 )
		
if __name__ == '__main__':
	unittest.main()