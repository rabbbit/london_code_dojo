import unittest

from pub import Glass

class TestGlass(unittest.TestCase):


	def setUp(self):
		self.glass = Glass(20)

	def test_canHaveDifferentMaxVolume(self):
		onePintInOunces = 20;
		halfPintInOunces = 10;

		onePintGlass = Glass(onePintInOunces)
		halfPintGlass = Glass(halfPintInOunces)

		onePintGlass.fill();
		halfPintGlass.fill();

		self.assertEqual(onePintGlass.volumeInOunces(), onePintInOunces)
		self.assertEqual(halfPintGlass.volumeInOunces(), halfPintInOunces)

	def test_shouldBeEmptyWhenItisCreated(self):
		self.assertTrue(self.glass.is_empty())

	def test_canBeFilled(self):

		glassIsEmpty = self.glass.is_empty()

		self.glass.fill()

		self.assertTrue(glassIsEmpty)
		self.assertFalse(self.glass.is_empty())

	def test_isFilledWithOnePint(self):
		expectedInitialVolumeInOunces = 0
		expectedVolumeInOunces = 20

		actualInitialVolumeInOunces = self.glass.volumeInOunces()
		self.glass.fill()
		actualVolumeInOunces = self.glass.volumeInOunces();

		self.assertEqual(actualInitialVolumeInOunces, expectedInitialVolumeInOunces)
		self.assertEqual(actualVolumeInOunces, expectedVolumeInOunces)

	def test_thatInitialVolumeDecreasesWhenCustomerDrinks(self):

		expectedVolumeBeforeDrink = 20
		expectedVolumeAfterDrink = 19
		
		self.glass.fill()
		actualVolumeBeforeDrink = self.glass.getCurrentLiquidInGlass()
		
		
		self.glass.drink()
		
		actualVolumeAfterDrink = self.glass.getCurrentLiquidInGlass()

		self.assertEquals(expectedVolumeBeforeDrink, actualVolumeBeforeDrink)
		self.assertEquals(expectedVolumeAfterDrink, actualVolumeAfterDrink)


if __name__ == '__main__':
	unittest.main()


