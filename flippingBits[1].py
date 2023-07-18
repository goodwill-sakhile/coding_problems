def solveFlippingBits(integer):
	bits = 31
	binary = ""
	while bits >= 0:
		division = integer//(2**(bits))
		if division > 0:
			binary += "1"
		else:
			binary += "0"
		integer = integer%(2**(bits))
		bits -= 1
	return binary
def flipBits(bin):
	new_bin = ""
	for bit in bin:
		if bit == "1":
			new_bin += "0"
		else:
			new_bin += "1"
	return new_bin
def getDecimalFromBinary(bin_string):
	bits = 31
	count = 0
	integer = 0
	while bits >= 0:
		if bin_string[count] == "1":
			integer += 2**(bits)
		else:
			integer += 0
		bits -= 1
		count += 1
	return integer
bin = solveFlippingBits(2147483647)
flipped_bits = flipBits(bin)
integer = getDecimalFromBinary(flipped_bits)
print(integer)