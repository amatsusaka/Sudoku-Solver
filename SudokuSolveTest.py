#!/usr/bin/python

import unittest
import SudokuSolve
from math import sqrt
from cStringIO import StringIO
import sys

########################################
#			Test Cases
########################################
class TestStuff(unittest.TestCase):
	def setUp(self):
		self.mySolver = SudokuSolve.Solver()

	def test_Solve(self):
		grid = [
			[1, 2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]
		expected = [[
			[1, 2, 3, 4], 
			[3, 4, 1, 2], 
			[4, 3, 2, 1], 
			[2, 1, 4, 3]
			]]
		self.mySolver.SetGrid(grid)
		actual = self.mySolver.Solve()
		self.assertEquals(actual, expected)
		
	def test_SetGrid(self):
		expected = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
		self.mySolver.SetGrid(expected)
		actual = self.mySolver.GetGrid()
		self.assertEquals(actual, expected)
		
	def test_GetGrid(self):
		expected = [
			[1, 2, 3, 4, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
			]
		self.mySolver.SetGrid(expected)
		actual = self.mySolver.GetGrid()
		self.assertEquals(actual, expected)
		
	def test_ReadGridFromFile(self):
		expected = [
			[1, 2, 0, 4],
			[3, 0, 0, 2],
			[0, 0, 0, 0],
			[2, 1, 0, 3]]
		actual = self.mySolver.ReadGridFromFile("TestCase1.txt")
		self.assertEquals(expected, actual)
	
	def test_FindPsbs(self):
		grid = [
			[1, 2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]

		expected = [1, 2, 4]
		
		actual = self.mySolver.FindPsbs(grid, 2, 2)

		self.assertEquals(actual, expected)
	
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
			
		self.assertEquals(array, checkArray)

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
		expected = [3, 4, 7, 8]
		
		actual = self.mySolver.BlockToArray( grid, 1 )

		self.assertEquals(actual, expected)
		
	def test_LocateNextEmpty(self):
		grid = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 0, 12],
			[13, 14, 15, 16]
			]
		val = self.mySolver.LocateNextEmpty( grid )

		self.assertEquals( val, [2,2] )
		
	def test_LocateBlock(self):
		grid = [
			[1, 2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]
		val = self.mySolver.LocateBlock( [0,3], sqrt( len( grid ) ) )

		self.assertEquals( val, 1 )
		
	def test_PrintGrid(self):
		grid = [
			[1, 2],
			[2, 1]
			]
		expected = "----------\n|  1   2   | \n|  2   1   | \n----------\n"
		
		# re-route print() output to a string instead
		stdout_saved, sys.stdout = sys.stdout, StringIO()
		self.mySolver.PrintGrid( grid );
		
		# get printed value, reset stdout
		actual = sys.stdout.getvalue()
		sys.stdout = stdout_saved
		
		self.assertEqual(actual, expected)
		
	def test_CleanRowPrint(self):
		grid_row = [1, 2]
		expected = "|  1   2   | \n"
		
		# re-route print() output to a string instead
		stdout_saved, sys.stdout = sys.stdout, StringIO()
		self.mySolver.CleanRowPrint(0, grid_row)
		
		# get printed value, reset stdout
		actual = sys.stdout.getvalue()
		sys.stdout = stdout_saved
		
		self.assertEqual(actual, expected)
		
	def test_ValidateGrid(self):
		good_grid = [
			[1, 2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]
		bad_grid = [
			[2, 0, 4], 
			[3, 0, 0, 2], 
			[0, 0, 0, 0], 
			[2, 1, 0, 3]
			]
		actual = self.mySolver.ValidateGrid( good_grid, 1, 1 )
		self.assertTrue(actual)
		
		actual = self.mySolver.ValidateGrid( bad_grid, 0, 0 )
		self.assertFalse(actual)
		
		#TODO: write tests for other bad grid permutations
		
	def test_CreatePsbGrid(self):
		self.assertTrue(False) #TODO: make this work
		
	def test_UpdatePsb(self):
		self.assertTrue(False) #TODO: make this work
		
	def test_FillGrid(self):
		self.assertTrue(False) #TODO: make this work
		
if __name__ == '__main__':
	unittest.main()