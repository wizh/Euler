import operator
num, digit = '', 0
while len(num) <= 1000000:
	num += str(digit)
	digit += 1

print reduce(operator.mul, [int(num[10**i]) for i in range(7)], 1)
