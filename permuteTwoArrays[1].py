def solvePermutingTwoArrays(_array_a, _array_b, k):
	chosen_indexes = []
	for i in range(len(_array_a)):
		element_partner = 0
		for j in range(len(_array_b)):
			sum = _array_a[i] + _array_b[j]
			if sum >= k:
				print(sum)
				if ((_array_b[j] < element_partner) and (element_partner > 0)):
					if j not in chosen_indexes:
						element_partner = _array_b[j]
						chosen_indexes.append(j)
				elif (element_partner == 0):
					if j not in chosen_indexes:
						element_partner = _array_b[j]
						chosen_indexes.append(j)
	print(chosen_indexes)
	if len(_array_a) != len(chosen_indexes):
		return "No"
	return "Yes"
print(solvePermutingTwoArrays([2, 1, 3], [7, 8, 9], 10))