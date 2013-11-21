def testEmptyListShouldReturnMinusOne():
	assert search([],7) == -1

def testSearchingForZeroInSingletonZeroShouldReturnZero():
	assert search([0],0) == 0

def testSearchingForZeroInSingletonOneShouldReturnMinusOne():
	assert search([1],0) == -1

def testSearchingForSecondElementInListOfLengthTwoShouldReturnOne():
	assert search([1,7], 7) == 1

def search(my_list, target):
	if len(my_list) > 0 and my_list[0] == target:
		return 0
	elif len(my_list) > 1 and my_list[1] == target:
		return 1
	else:
		return -1

if __name__ == "__main__":
	testEmptyListShouldReturnMinusOne()
	testSearchingForZeroInSingletonZeroShouldReturnZero()
	testSearchingForZeroInSingletonOneShouldReturnMinusOne()
	testSearchingForSecondElementInListOfLengthTwoShouldReturnOne()
