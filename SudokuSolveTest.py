#!/usr/bin/python

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
		grid_1 = [4, 8, 9, 2, 1, 3] #should pass
		grid_2 = [8, 8, 2, 1, 3, 9] #should fail
		
		self.assertTrue( self.mySolver.CheckArray( grid_1 ) )
		self.assertFalse( self.mySolver.CheckArray( grid_2 ) )

	def test_ColToArray(self):
		#print "Testing column to array..."
		grid = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
		checkArray = [1, 6, 11, 16, 21]
		
		array = self.mySolver.ColToArray( grid, 0 )
			
		self.assertTrue(array == checkArray)

	def test_CheckGridDimensions(self):
		#print "Testing grid validation..."
		grid_1 = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
		self.assertFalse( self.mySolver.CheckGridDimensions( grid_1 ) )
		
		grid_2 = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
			]
		self.assertTrue( self.mySolver.CheckGridDimensions( grid_2 ) )
		
	def test_BlockToArray(self):
		#print "Testing blcok to array..."
		grid = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
			]
		checkArray = [3, 4, 7, 8]
		
		array = self.mySolver.BlockToArray( grid, 1 )

		self.assertTrue(array == checkArray)
		
	def test_LocateNextEmpty(self):
		grid = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 0, 12],
			[13, 14, 15, 16]
			]
		val = self.mySolver.LocateNextEmpty( grid )

		self.assertTrue( val == [2,2] )
		
	def test_LocateBlock(self):
		grid = [
			[1, 2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]
		val = self.mySolver.LocateBlock( [0,3], sqrt( len( grid ) ) )

		self.assertTrue( val == 1 )
		
if __name__ == '__main__':
	unittest.main()