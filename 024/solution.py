perms = []
digits = '0123456789'

for d in digits:
    perms.append([d])

for i in range(1, 10):
    for d in digits:
        for p in perms:
            if not d in p and len(p) == i:
                perms.append(p + [d])

perms = filter(lambda x: len(x) == 10, perms)
print sorted(map((lambda x: int(''.join(x))), perms))[1000000-1]
