# Code for linear search

def linear(data: list, value):
	for element in data:
		if element == value:
			print("Value found")
			break
	else:
		print("Value not found")


linear([1,2,3,4,5,6,78,9,9,45,7,6,4,345,234], 4)