#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
	result = []
	
	for n in range(0, list_length):
		try:
			a = my_list_1[n]
			b = my_list_2[n]
			q = 0
			if not isinstance(a, (int, float)) or not isinstance (b, (int, float)):
				print("wrong type")
			elif b == 0:
				print("division by 0")
			else:
				q = a / b
			result.append(q)
		except IndexError as e:
			print("out of range")
			result.append(0)
	return result
