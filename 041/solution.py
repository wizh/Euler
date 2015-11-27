# Answer must be 7 digits long (can be shown mathematically)
from math import sqrt

perms = []
digits = '1234567'

for d in digits:
    perms.append([d])

for i in range(1, 7):
    for d in digits:
        for p in perms:
            if not d in p and len(p) == i:
               perms.append(p + [d])

perms = map(lambda x: int(''.join(x)), filter(lambda x:len(x) == 7, perms))
print max(filter(lambda x: x % 2 and all(x % j for j in
                                     xrange(3, int(sqrt(x) - 1), 2)), perms))
