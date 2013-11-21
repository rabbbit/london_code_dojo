class Glass(object):

	def __init__(self, maxVolume):
		self._maxVolume = maxVolume
		self.volume = 0

	def is_empty(self):
		return self.volume == 0

	def fill(self):
		self.volume = self._maxVolume 

	def volumeInOunces(self):
		return self.volume

	def drink(self):
		self.volume -= 1  

	def getCurrentLiquidInGlass(self):
		return self.volume







