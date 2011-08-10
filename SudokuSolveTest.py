import unittest

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
	val = self.LocateBlock( [0,3], sqrt( len( grid ) ) )
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