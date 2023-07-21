def solveCountSort(_array):
	max_value = max(_array)
	zeros_array = []
	for i in range(max_value + 1):
		zeros_array.append(0)
	for index in _array:
		zeros_array[index] = zeros_array[index] + 1
	return zeros_array
print(solveCountSort([1, 1, 3, 2, 1]))