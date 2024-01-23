#!/usr/bin/python3

"""Shape definition."""
class Square:
	"""Represent the shape."""
	def __init__(self, size=0):
		"""Initialize the shape."""
		self.size = size
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
	def area(self):
		"""area of shape."""
		return self.__size * self.__size
	def my_print(self):
		"""Print square."""
		for i in range(0, self.__size):
			[print("#", end="") for j in range(self.__size)]
			print("")
		if self.__size == 0:
			print("")
