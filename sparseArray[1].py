def solveSparseArrays(_strings, _queries):
	count_list = []
	for query_element in _queries:
		count = 0
		for string_element in _strings:
			if string_element == query_element:
				count += 1
		count_list.append(count)
	print(count_list)
solveSparseArrays(["ab", "ab", "abc"], ["ab", "abc", "bc"])