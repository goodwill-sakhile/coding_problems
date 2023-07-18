def solveMinMaxSum(_array):
	min_sum_value = -1
	max_sum_value  = -1
	for i in range(len(_array)):
		sum = 0
		for j in range(len(_array)):
			if j != i:
				sum += _array[j]
		if ((min_sum_value == -1) and (max_sum_value == -1)):
			min_sum_value = sum
			max_sum_value  = sum
		else:
			if sum <= min_sum_value:
				min_sum_value = sum
			elif sum >= max_sum_value:
				max_sum_value = sum
	print(min_sum_value, max_sum_value)
solveMinMaxSum([1, 2, 3, 4, 5])