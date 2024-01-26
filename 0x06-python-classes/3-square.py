#!/usr/bin/python3

"""Defines a Shape."""
class Square:
	"""shape representation."""
	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			"""find value error."""
			raise ValueError("size must be >= 0")
		self.__size = size
	def area(self):
		"""Return area of square."""
		return (self.__size * self.__size)
