def setPrecision(decimal, place):
	dot_index = decimal.find(".")
	if (len(decimal) - dot_index > place):
		print(decimal[0:dot_index] + decimal[dot_index:dot_index + place])
	elif ((len(decimal) - dot_index) < place):
		zeros = "0"
		for i in range(place - (len(decimal) - dot_index)):
			zeros += "0"
		print(decimal + zeros)
	else:
		print(decimal)
def solvePlusMinus(_array):
	positive_number = 0
	negative_number = 0
	zero = 0
	for element in _array:
		if element > 0:
			positive_number += 1
		elif element < 0:
			negative_number += 1
		elif element == 0:
			zero  += 1
	setPrecision(str(positive_number/float(len(_array))), 6)
	setPrecision(str(negative_number/float(len(_array))), 6)
	setPrecision(str(zero/float(len(_array))), 6)
solvePlusMinus([1, 1, 0, -1, -1])