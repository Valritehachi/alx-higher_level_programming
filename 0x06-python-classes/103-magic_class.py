#!/usr/bin/python3

"""Define Math."""

import math
class MagicClass:
	"""showas shape."""
	def __init__(self, radius=0):
		"""shape initialized"""        
		self.__radius = 0
		if type(radius) is not int and type(radius) is not float:
			raise TypeError("radius must be a number")
		self.__radius = radius
	def area(self):
		"""area of shape."""
		return (self.__radius ** 2 * math.pi)
	def circumference(self):
		"""circumference of shape."""
		return (2 * math.pi * self.__radius)
