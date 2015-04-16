with open ("input.txt") as f:
    l = f.read().replace('\n', '')

maxprod = 0
for i in range(len(l) - 12):
    prod = 1
    for j in range(0, 13):
        prod *= int(l[i + j])

    maxprod = max(maxprod, prod)

print(maxprod)