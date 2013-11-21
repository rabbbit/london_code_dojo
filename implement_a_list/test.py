def testEmptyListShouldReturnMinusOne():
	assert search([],7) == -1

def testSearchingForZeroInSingletonZeroShouldReturnZero():
	assert search([0],0) == 0

def testSearchingForZeroInSingletonOneShouldReturnMinusOne():
	assert search([1],0) == -1

def testSearchingForSecondElementInListOfLengthTwoShouldReturnOne():
	assert search([1,7], 7) == 1

def testSearchingForNInRangeOneHundredShouldReturnN(max):
	for n in range(max):
		assert search(range(max), n) == n, "Could not find " + str(n) + "in range(" \
		+ str(max) + ")"

def testSearchingInRandomList():
	assert search([-5, 7, 32, 100, 2356], 100) == 3
	assert search([-5, 7, 32, 100, 2356], 2356) == 4

def testMiddleIndexOfEmptyListShouldReturnMinusOne():
	assert split([]) == -1

def testMiddleOfRangeMaxShouldBeMaxOverTwo(max):
	assert split(range(max)) == max / 2

def testSearchPortionOnEmptyListShouldReturnMinusOne():
	assert searchPortion([], 0, 0, 7) == -1

def testSearchPortionWhenValueIsThere():
	assert searchPortion([1, 3, 5, 7, 99], 1, 3, 5) == 2

def testSearchPortionWhenValueIsNotThere():
	assert searchPortion([1, 566, 1000, 2222], 1, 3, 1) == -1

def testSearchingForZeroInSingletonZero():
	assert searchPortion([0], 0, 0, 0) == 0

def testFindingMiddleIntegerForZeros():
	assert findMiddle(0,0) == 0

def testFindingMiddleIntegerForNormalList():
	for i in range(max):
		assert findMiddle(1,i) == (1+i)/2

def search(my_list, target):
	if not my_list:
		return -1
	if target < my_list[split(my_list)]:
		print "Searching left"
		return searchPortion(my_list, 0, split(my_list) - 1, target)
	else:
		print "Searching from " + str(split(my_list)) + " to " + \
		str(len(my_list) - 1)
		return searchPortion(my_list, split(my_list), len(my_list) - 1, target)

def search_(my_list, target):
	for i in range(len(my_list)):
		if my_list[i] == target:
			return i
	else:
		return -1
	
def searchPortion(my_list, leftIndex, rightIndex, target):
	index = search_(my_list, target)

	if not leftIndex <= index <= rightIndex:
		return -1

	return index

def split(my_list):

	if not my_list:
		return -1

	return len(my_list)/2

def findMiddle(leftIndex, rightIndex):
	return 0

if __name__ == "__main__":
	testEmptyListShouldReturnMinusOne()
	testSearchingForZeroInSingletonZero()
	testSearchingForZeroInSingletonZeroShouldReturnZero()
	testSearchingForZeroInSingletonOneShouldReturnMinusOne()
	testSearchingForSecondElementInListOfLengthTwoShouldReturnOne()
	max = input("Enter maximum value")
	testSearchingForNInRangeOneHundredShouldReturnN(max)
	testMiddleIndexOfEmptyListShouldReturnMinusOne()
	testMiddleOfRangeMaxShouldBeMaxOverTwo(max)
	testSearchPortionOnEmptyListShouldReturnMinusOne()
	testSearchPortionWhenValueIsNotThere()
	testSearchPortionWhenValueIsThere()
	testFindingMiddleIntegerForZeros()
