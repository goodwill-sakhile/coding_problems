def solvePangrams(_string):
	alphabet = "abcdefghijjklmnopqrstuvwxyz"
	for element in _string:
		if element in alphabet:
			alphabet = alphabet[0:alphabet.find(element)] + alphabet[alphabet.find(lement) + 1:]
	if alphabet == "":
		return "Panagram"
	else:
		return "Not Panagram"