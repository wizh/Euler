res, a, b = 0, 0, 1

while res <= 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        res += b
print(res)
