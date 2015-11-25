total, current = 0, 1
for i in range(1, 501):
	for j in range(4):
		current += i * 2
		total += current	

print total + 1
