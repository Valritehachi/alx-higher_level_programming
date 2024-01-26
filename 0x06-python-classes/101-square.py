#!/usr/bin/python3

"""Define shape."""
class Square:
	"""shape represented."""
	def __init__(self, size=0, position=(0, 0)):
		self.size = size
		self.position = position
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
	@property
	def position(self):
		"""position."""
		return (self.__position)

	@position.setter
	def position(self, value):
		"""position setter"""
		if (not isinstance(value, tuple) or len(value) != 2 or	not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value
	def area(self):
		"""shape ares."""
		return (self.__size * self.__size)
	def my_print(self):
		"""print."""
		if self.__size == 0:
			print("")
			return
