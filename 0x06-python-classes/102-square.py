#!/usr/bin/python3

"""Define shape."""
class Square:
	"""shape represented."""
	def __init__(self, size=0):
		self.size = size

	@property
	def size(self):
		"""size."""
		return (self.__size)

	@size.setter
	def size(self, value):
		"""sets size"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""The area."""
		return (self.__size * self.__size)
	def __eq__(self, other):
		"""same size as shape."""
		return self.area() == other.area()
	def __lt__(self, other):
		"""less than Shape."""
		return self.area() < other.area()
	def __ne__(self, other):
		"""not equal to shape."""
		return self.area() != other.area()
	def __le__(self, other):
		"""less than or equal to shape size."""
		return self.area() <= other.area()
	def __gt__(self, other):
		"""greater than shape."""
		return self.area() > other.area()
	def __ge__(self, other):
		"""greater than or equal to shape."""
		return self.area() >= other.area()
