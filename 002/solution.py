sum, a, b = 0, 0, 1

while sum <= 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        sum += b
print(sum)