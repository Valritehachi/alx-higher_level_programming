#!/usr/bin/python3

"""Shape definition."""
class Square:
	"""Represent the shape."""
	def __init__(self, size=0, position=(0, 0)):
		"""Initialize the shape."""
		self.size = size
		self.position = position
	@property
	def size(self):
		"""return size of shape."""
		return self.__size
	@size.setter
	def size(self, value):
		"""return size of shape."""        
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value
		"""get position"""
	@property
	def position(self):
		"""position of shape."""
		return self.__position
	@position.setter
	def position(self, value):
		if not isinstance(value, tuple)or len(value) != 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value
	def my_print(self):
		"""Print shape."""
		if self.__size == 0:
			print("")
		else:
			for _ in range(self.__position[1]):
				print("")
			for _ in range(self.__size):
				print(" " * self.__position[0] + "#" * self.__size)
