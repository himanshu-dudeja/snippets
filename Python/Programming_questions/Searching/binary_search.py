# Code for binary Search

def binary_search(data: list, value)-> None:
	if len(data) == 1 and value != data[0]:
		print("Not Found")
		exit()
	mid_point = len(data) // 2
	if value == data[mid_point]:
		print("Value Found")
		exit()
	elif value > data[mid_point]:
		data = data[mid_point:]
		binary_search(data, value)
	elif value < data[mid_point]:
		data = data[:mid_point]
		binary_search(data, value)
	else:
		print("Value Not Found")

binary_search([1,2,3,4,5,6,7,8,9], 88)