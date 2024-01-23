#!/usr/bin/python3

"""Defines a class."""

class Square:
	"""shows a shape"""
	def __init__(self, size=0):
		"""starts up a shape"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
