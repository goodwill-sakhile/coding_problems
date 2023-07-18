def solveLonelyInteger(_array):
	for i in range(len(_array)):
		occurance = 0
		for j in range(len(_array)):
			if _array[i] == _array[j]:
				occurance += 1
		if occurance == 1:
			print(_array[i])
solveLonelyInteger([1, 2, 3, 4, 3, 2, 1])