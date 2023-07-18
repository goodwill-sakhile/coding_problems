def solveDiagonalDifference(_matrix_array):
	count_one = 0
	count_two = -1	
	sum_one = 0
	sum_two = 0
	for array in _matrix_array:
		sum_one += array[count_one]
		sum_two += array[count_two]
		count_one += 1
		count_two -= 1
	return abs(sum_one - sum_two)
abs_difference = solveDiagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(abs_difference)